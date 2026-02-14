<?php
/**
 * Page template.
 *
 * @package tutoline
 */

get_header();
?>
<main id="main-content" class="section">
  <article class="glass course-detail">
    <h1><?php the_title(); ?></h1>
    <?php while (have_posts()) : the_post(); the_content(); endwhile; ?>
  </article>
</main>
<?php get_footer(); ?>
