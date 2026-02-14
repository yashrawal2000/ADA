<?php
/**
 * Single course template.
 *
 * @package tutoline
 */

get_header();
?>
<main id="main-content" class="section">
  <?php while (have_posts()) : the_post(); ?>
    <article class="glass course-detail">
      <p><strong><?php esc_html_e('Category:', 'tutoline'); ?></strong> <?php esc_html_e('Cybersecurity Professional Track', 'tutoline'); ?></p>
      <h1><?php the_title(); ?></h1>
      <?php the_content(); ?>
      <a class="enroll-btn" href="<?php echo esc_url(home_url('/#pricing')); ?>"><?php esc_html_e('Enroll with Tutoline', 'tutoline'); ?></a>
    </article>
  <?php endwhile; ?>
</main>
<?php get_footer(); ?>
