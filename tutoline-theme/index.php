<?php
/**
 * Default template.
 *
 * @package tutoline
 */

get_header();
?>
<main id="main-content" class="posts-list">
  <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
    <article class="glass" style="padding:1.2rem; margin-bottom:1rem;">
      <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
      <p><?php the_excerpt(); ?></p>
    </article>
  <?php endwhile; the_posts_pagination(); else : ?>
    <article class="glass" style="padding:1.2rem;"><?php esc_html_e('No content found.', 'tutoline'); ?></article>
  <?php endif; ?>
</main>
<?php get_footer(); ?>
