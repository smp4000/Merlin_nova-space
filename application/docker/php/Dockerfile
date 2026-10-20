FROM php:8.4.26-cli-bookworm@sha256:836ac6c672d1372a47c8fd61b625015bd07760f493fb2eaab2087636498a2b4b
RUN --mount=type=secret,id=proxy_ca,target=/usr/local/share/ca-certificates/cloud-proxy.crt \
    update-ca-certificates && sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources \
    && apt-get update && apt-get install -y --no-install-recommends git unzip libicu-dev libzip-dev libonig-dev libpng-dev libxml2-dev \
    && docker-php-ext-install -j4 pdo_mysql mbstring intl zip bcmath gd pcntl \
    && rm -rf /var/lib/apt/lists/*
COPY --from=composer:2.10.3@sha256:af98f42dfff7c68ba8d53c2164fd9fde1087b7d449514baa38c418b1f6bc4bac /usr/bin/composer /usr/local/bin/composer
WORKDIR /app
