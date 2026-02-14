<?php
/**
 * Tutoline theme setup.
 *
 * @package tutoline
 */

if (! defined('ABSPATH')) {
    exit;
}

require_once get_template_directory() . '/inc.php';

function tutoline_theme_setup()
{
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('custom-logo');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script']);

    register_nav_menus([
        'primary' => __('Primary Menu', 'tutoline'),
    ]);
}
add_action('after_setup_theme', 'tutoline_theme_setup');

function tutoline_enqueue_assets()
{
    wp_enqueue_style('tutoline-style', get_stylesheet_uri(), [], wp_get_theme()->get('Version'));
    wp_enqueue_script('tutoline-script', get_template_directory_uri() . '/assets/js/theme.js', [], wp_get_theme()->get('Version'), true);
}
add_action('wp_enqueue_scripts', 'tutoline_enqueue_assets');

function tutoline_register_cpts()
{
    register_post_type('tutoline_course', [
        'labels' => [
            'name' => __('Courses', 'tutoline'),
            'singular_name' => __('Course', 'tutoline'),
        ],
        'public' => true,
        'has_archive' => true,
        'menu_icon' => 'dashicons-welcome-learn-more',
        'rewrite' => ['slug' => 'courses'],
        'supports' => ['title', 'editor', 'excerpt', 'thumbnail'],
        'show_in_rest' => true,
    ]);

    register_post_type('tutoline_service', [
        'labels' => [
            'name' => __('Services', 'tutoline'),
            'singular_name' => __('Service', 'tutoline'),
        ],
        'public' => true,
        'has_archive' => false,
        'menu_icon' => 'dashicons-shield-alt',
        'rewrite' => ['slug' => 'services'],
        'supports' => ['title', 'editor', 'excerpt'],
        'show_in_rest' => true,
    ]);
}
add_action('init', 'tutoline_register_cpts');
