<?php

namespace Tests\Feature;

use App\Models\User;
use Filament\Auth\Pages\Login;
use Filament\Facades\Filament;
use Illuminate\Database\QueryException;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Support\Facades\DB;
use Livewire\Livewire;
use Tests\TestCase;

class AdminAccessTest extends TestCase
{
    use DatabaseTransactions;

    protected function setUp(): void
    {
        parent::setUp();
        $this->assertSame('mysql', DB::connection()->getDriverName());
        $this->assertSame('merlin_nova_test', DB::selectOne('SELECT DATABASE() AS name')->name);
        config(['local-admin.email' => 'admin@merlin.invalid']);
        Filament::setCurrentPanel(Filament::getPanel('admin'));
    }

    public function test_test_database_user_cannot_read_the_development_database(): void
    {
        try {
            DB::select('SELECT COUNT(*) FROM merlin_nova_dev.users');
            $this->fail('Test user unexpectedly has access to development data.');
        } catch (QueryException $exception) {
            $this->assertSame(1142, $exception->errorInfo[1]);
        }
    }

    public function test_guests_are_redirected_and_registration_is_absent(): void
    {
        $this->get('/admin')->assertRedirect('/admin/login');
        $this->get('/admin/login')->assertOk();
        $this->get('/admin/register')->assertNotFound();
    }

    public function test_an_ordinary_authenticated_user_cannot_open_the_panel(): void
    {
        $user = User::factory()->create(['email' => 'ordinary@example.invalid']);
        $this->actingAs($user)->get('/admin')->assertForbidden();
    }

    public function test_only_the_configured_local_admin_can_log_in(): void
    {
        $password = bin2hex(random_bytes(24));
        $admin = User::factory()->create(['email' => 'admin@merlin.invalid', 'password' => $password]);
        Livewire::test(Login::class)
            ->set('data.email', $admin->email)
            ->set('data.password', $password)
            ->call('authenticate')
            ->assertHasNoErrors();
        $this->assertAuthenticatedAs($admin);
        $this->get('/admin')->assertOk();
    }

    public function test_valid_credentials_of_an_ordinary_user_are_rejected(): void
    {
        $password = bin2hex(random_bytes(24));
        $user = User::factory()->create(['email' => 'ordinary@example.invalid', 'password' => $password]);
        Livewire::test(Login::class)
            ->set('data.email', $user->email)
            ->set('data.password', $password)
            ->call('authenticate')
            ->assertHasErrors(['data.email']);
        $this->assertGuest();
    }

    public function test_the_local_admin_is_not_authorized_in_production(): void
    {
        $user = User::factory()->make(['email' => 'admin@merlin.invalid']);
        $this->app->instance('env', 'production');
        $this->assertFalse($user->canAccessPanel(Filament::getPanel('admin')));
    }
}
