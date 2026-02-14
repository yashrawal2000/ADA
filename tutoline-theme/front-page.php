<?php
/**
 * Front page template.
 *
 * @package tutoline
 */

get_header();
?>
<main id="main-content">
  <section class="hero">
    <div class="hero-content glass">
      <p class="eyebrow"><?php esc_html_e('Future-ready Learning Platform', 'tutoline'); ?></p>
      <h1><?php esc_html_e('Master Cybersecurity in Tutoline’s', 'tutoline'); ?> <span><?php esc_html_e('Neon Learning Universe', 'tutoline'); ?></span></h1>
      <p><?php esc_html_e('A high-tech learning experience combining immersive labs, expert mentorship, and enterprise security services.', 'tutoline'); ?></p>
      <div class="hero-actions">
        <a class="enroll-btn" href="#courses"><?php esc_html_e('Explore Courses', 'tutoline'); ?></a>
        <button class="ghost-btn" id="previewTrigger" type="button"><?php esc_html_e('Interactive Course Preview', 'tutoline'); ?></button>
      </div>
      <div class="hero-metrics">
        <article><strong>45k+</strong><span><?php esc_html_e('Learners', 'tutoline'); ?></span></article>
        <article><strong>1,200+</strong><span><?php esc_html_e('Enterprise Clients', 'tutoline'); ?></span></article>
        <article><strong>98%</strong><span><?php esc_html_e('Completion Success', 'tutoline'); ?></span></article>
      </div>
    </div>
    <aside class="hero-side">
      <article class="holo-card"><h3><?php esc_html_e('3D Code Matrix', 'tutoline'); ?></h3><p><?php esc_html_e('Visual secure code intelligence for advanced labs.', 'tutoline'); ?></p></article>
      <article class="holo-card"><h3><?php esc_html_e('Neural Threat Graph', 'tutoline'); ?></h3><p><?php esc_html_e('Attack path mapping and live defense simulations.', 'tutoline'); ?></p></article>
    </aside>
  </section>

  <section class="section" id="courses">
    <div class="section-title">
      <h2><?php esc_html_e('Courses Category', 'tutoline'); ?></h2>
      <p><?php esc_html_e('SEO-friendly cybersecurity programs for modern security careers.', 'tutoline'); ?></p>
    </div>
    <div class="course-grid">
      <?php
      $courses = new WP_Query([
          'post_type'      => 'tutoline_course',
          'posts_per_page' => 15,
      ]);
      if ($courses->have_posts()) :
          while ($courses->have_posts()) :
              $courses->the_post();
              ?>
              <a class="course-card glass" href="<?php the_permalink(); ?>">
                <h3><?php the_title(); ?></h3>
                <p><?php echo esc_html(wp_trim_words(get_the_excerpt(), 18)); ?></p>
              </a>
              <?php
          endwhile;
      else :
          ?>
          <article class="course-card glass">
            <h3><?php esc_html_e('Add your first course from WordPress Admin → Courses', 'tutoline'); ?></h3>
            <p><?php esc_html_e('You can create 15+ course pages with SEO-friendly descriptions and featured images.', 'tutoline'); ?></p>
          </article>
      <?php endif; wp_reset_postdata(); ?>
    </div>
  </section>

  <section class="section" id="learning">
    <div class="section-title"><h2><?php esc_html_e('Learning Journey', 'tutoline'); ?></h2></div>
    <div class="timeline-grid">
      <article class="glass"><h3><?php esc_html_e('Step 1: Skill Assessment', 'tutoline'); ?></h3><p><?php esc_html_e('Adaptive pre-test maps your level and recommends the right track.', 'tutoline'); ?></p></article>
      <article class="glass"><h3><?php esc_html_e('Step 2: Guided Labs', 'tutoline'); ?></h3><p><?php esc_html_e('Hands-on scenarios with secure coding tasks and red/blue exercises.', 'tutoline'); ?></p></article>
      <article class="glass"><h3><?php esc_html_e('Step 3: Mentor Review', 'tutoline'); ?></h3><p><?php esc_html_e('1:1 feedback on reports, exploit logic, and remediation quality.', 'tutoline'); ?></p></article>
      <article class="glass"><h3><?php esc_html_e('Step 4: Certification & Placement', 'tutoline'); ?></h3><p><?php esc_html_e('Portfolio-ready projects and career-focused preparation.', 'tutoline'); ?></p></article>
    </div>
  </section>

  <section class="section" id="services">
    <div class="section-title"><h2><?php esc_html_e('Security Services We Offer', 'tutoline'); ?></h2></div>
    <div class="service-grid">
      <?php
      $services = new WP_Query([
          'post_type'      => 'tutoline_service',
          'posts_per_page' => 6,
      ]);
      if ($services->have_posts()) :
          while ($services->have_posts()) :
              $services->the_post();
              ?>
              <article class="glass">
                <h3><?php the_title(); ?></h3>
                <p><?php echo esc_html(wp_trim_words(get_the_excerpt() ?: get_the_content(null, false), 22)); ?></p>
              </article>
              <?php
          endwhile;
      else :
          ?>
          <article class="glass"><h3>Vulnerability Assessment (VA)</h3><p><?php esc_html_e('Add services from WordPress Admin → Services.', 'tutoline'); ?></p></article>
      <?php endif; wp_reset_postdata(); ?>
    </div>
  </section>

  <section class="section" id="pricing">
    <div class="section-title"><h2><?php esc_html_e('Pricing Plans', 'tutoline'); ?></h2></div>
    <div class="pricing-grid">
      <article class="glass"><h3><?php esc_html_e('Starter', 'tutoline'); ?></h3><p class="price">$49/mo</p></article>
      <article class="glass featured"><h3><?php esc_html_e('Pro', 'tutoline'); ?></h3><p class="price">$129/mo</p></article>
      <article class="glass"><h3><?php esc_html_e('Enterprise', 'tutoline'); ?></h3><p class="price"><?php esc_html_e('Custom', 'tutoline'); ?></p></article>
    </div>
  </section>

  <section class="section" id="blog">
    <div class="section-title"><h2><?php esc_html_e('Blog & Resources', 'tutoline'); ?></h2></div>
    <div class="resource-grid">
      <?php
      $posts = new WP_Query(['post_type' => 'post', 'posts_per_page' => 3]);
      if ($posts->have_posts()) :
          while ($posts->have_posts()) : $posts->the_post(); ?>
            <article class="glass">
              <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
              <p><?php echo esc_html(wp_trim_words(get_the_excerpt(), 20)); ?></p>
            </article>
          <?php endwhile;
      else : ?>
        <article class="glass"><h3><?php esc_html_e('Publish blog posts to show resources here.', 'tutoline'); ?></h3></article>
      <?php endif; wp_reset_postdata(); ?>
    </div>
  </section>

  <section class="section" id="contact">
    <div class="section-title"><h2><?php esc_html_e('Talk to Tutoline', 'tutoline'); ?></h2></div>
    <div class="glass contact-form">
      <?php
      if (shortcode_exists('contact-form-7')) {
          echo do_shortcode('[contact-form-7 id="1" title="Tutoline Contact"]');
      } else {
          echo '<p>' . esc_html__('Install a form plugin (like Contact Form 7) and place your shortcode here.', 'tutoline') . '</p>';
      }
      ?>
    </div>
  </section>
</main>

<div class="modal" id="previewModal" aria-hidden="true" role="dialog" aria-labelledby="previewTitle">
  <div class="modal-panel glass" tabindex="-1">
    <h3 id="previewTitle"><?php esc_html_e('Interactive Course Preview', 'tutoline'); ?></h3>
    <p><?php esc_html_e('Preview a simulated cyber lab with exploit analysis, secure patching tasks, and AI mentor feedback.', 'tutoline'); ?></p>
    <button class="enroll-btn" id="closeModal" type="button"><?php esc_html_e('Close Preview', 'tutoline'); ?></button>
  </div>
</div>
<?php
get_footer();
