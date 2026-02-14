<?php
/**
 * Helper functions.
 *
 * @package tutoline
 */

if (! defined('ABSPATH')) {
    exit;
}

function tutoline_nav_fallback()
{
    $links = [
        '#courses'  => __('Courses', 'tutoline'),
        '#learning' => __('Learning Path', 'tutoline'),
        '#services' => __('Services', 'tutoline'),
        '#pricing'  => __('Pricing', 'tutoline'),
        '#faq'      => __('FAQ', 'tutoline'),
        '#blog'     => __('Resources', 'tutoline'),
        '#contact'  => __('Contact', 'tutoline'),
    ];

    foreach ($links as $href => $label) {
        printf('<a href="%1$s">%2$s</a>', esc_url($href), esc_html($label));
    }
}
