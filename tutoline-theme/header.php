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
  <?php // Security headers should be sent by the web server, not via meta tags. ?>
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
