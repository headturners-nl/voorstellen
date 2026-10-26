<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="<?php echo esc_url( get_template_directory_uri() ); ?>/logo-mark.svg" type="image/svg+xml">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="site">
<div class="wrap nav">
<a class="brand" href="<?php echo esc_url( home_url() ); ?>/" aria-label="Headturners, naar de homepage"><svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="13" fill="#FFCF4A"/><path d="M7.5 18.5c1.8-1.3 3-1.3 4.2 0M7.5 24h3.6M7.5 29.5c1.8 1.3 3 1.3 4.2 0" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round"/><ellipse cx="21.5" cy="24" rx="6.2" ry="8.2" fill="#fff" stroke="#1F2A44" stroke-width="2.8"/><ellipse cx="34.5" cy="24" rx="6.2" ry="8.2" fill="#fff" stroke="#1F2A44" stroke-width="2.8"/><circle cx="24.6" cy="25" r="3.2" fill="#1F2A44"/><circle cx="37.6" cy="25" r="3.2" fill="#1F2A44"/><circle cx="25.5" cy="23.7" r="1" fill="#fff"/><circle cx="38.5" cy="23.7" r="1" fill="#fff"/></svg><span class="brand-name"><b>Headturners</b><i>Brands that make people look twice</i></span></a>
<button class="burger" type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="menu" id="menu" aria-label="Hoofdmenu">
<div class="dd"><button type="button" aria-expanded="false">Diensten <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-panel"><a href="<?php echo esc_url( home_url() ); ?>/websites/"><b>Websites</b><span>Laten bouwen, kopen of huren</span></a><a href="<?php echo esc_url( home_url() ); ?>/advertenties/"><b>Advertenties</b><span>Google Ads en Meta Ads</span></a><a href="<?php echo esc_url( home_url() ); ?>/social-en-blogs/"><b>Social media en blogs</b><span>Content die je vindbaar maakt</span></a><a href="<?php echo esc_url( home_url() ); ?>/branding/"><b>Branding</b><span>Logo, kleuren, visie en missie</span></a></div></div>
<a href="<?php echo esc_url( home_url() ); ?>/voorbeelden/">Voorbeelden</a>
<a href="<?php echo esc_url( home_url() ); ?>/websites/#prijzen">Prijzen</a>
<a href="<?php echo esc_url( home_url() ); ?>/over/">Over mij</a>
<a href="<?php echo esc_url( home_url() ); ?>/contact/">Contact</a>
<a class="btn btn-sun" href="<?php echo esc_url( home_url() ); ?>/contact/">Gratis voorstel</a>
</nav>
</div>
</header>
<main id="top">
