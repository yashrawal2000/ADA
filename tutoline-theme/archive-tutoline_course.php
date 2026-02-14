<?php
/**
 * Course archive template.
 *
 * @package tutoline
 */

get_header();
?>
<main id="main-content" class="section">
  <div class="section-title">
    <h1><?php esc_html_e('Courses', 'tutoline'); ?></h1>
  </div>
  <div class="course-grid">
    <?php while (have_posts()) : the_post(); ?>
      <a class="course-card glass" href="<?php the_permalink(); ?>">
        <h3><?php the_title(); ?></h3>
        <p><?php echo esc_html(wp_trim_words(get_the_excerpt(), 20)); ?></p>
      </a>
    <?php endwhile; ?>
  </div>
  <?php the_posts_pagination(); ?>
</main>
<?php get_footer(); ?>
