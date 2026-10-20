<?php

use App\Models\User;
use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');

Artisan::command('merlin:create-local-admin', function () {
    if (! app()->environment('local') || ! config('local-admin.email')) {
        $this->error('Only available locally with LOCAL_ADMIN_EMAIL configured.');

        return 1;
    }

    $path = base_path('.local/admin-password');
    if (! is_readable($path) || strlen(trim(file_get_contents($path))) < 24) {
        $this->error('Run python3 bin/prepare-local.py first.');

        return 1;
    }

    User::firstOrCreate(
        ['email' => config('local-admin.email')],
        ['name' => 'Local Technical Admin', 'password' => trim(file_get_contents($path))],
    );
    $this->info('Local admin exists. Existing accounts and passwords were preserved.');
})->purpose('Create the explicitly authorized local technical admin without printing credentials');
