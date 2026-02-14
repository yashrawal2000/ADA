<?php
/**
 * Header template.
 *
 * @package tutoline
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="<?php echo esc_attr(get_bloginfo('description')); ?>" />
  <meta name="robots" content="index, follow" />
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self'; font-src 'self' https: data:; object-src 'none'; media-src 'self'; frame-src 'none'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests" />
  <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin" />
  <meta http-equiv="X-Content-Type-Options" content="nosniff" />
  <meta http-equiv="X-Frame-Options" content="DENY" />
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="skip-link" href="#main-content"><?php esc_html_e('Skip to main content', 'tutoline'); ?></a>
<header class="site-header">
  <a href="<?php echo esc_url(home_url('/')); ?>" class="brand">tuto<span>line</span></a>
  <nav class="nav-links" aria-label="<?php esc_attr_e('Main navigation', 'tutoline'); ?>">
    <?php
    wp_nav_menu([
        'theme_location' => 'primary',
        'container'      => false,
        'fallback_cb'    => 'tutoline_nav_fallback',
        'items_wrap'     => '%3$s',
    ]);
    ?>
  </nav>
  <a class="enroll-btn" href="#pricing"><?php esc_html_e('Enroll Now', 'tutoline'); ?></a>
</header>
