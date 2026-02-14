'use strict';

const modal = document.getElementById('previewModal');
const trigger = document.getElementById('previewTrigger');
const closeBtn = document.getElementById('closeModal');
const modalPanel = document.querySelector('.modal-panel');
const contactForm = document.querySelector('.contact-form');
const formStatus = document.getElementById('form-status');
let lastFocusedElement = null;

const closeModal = () => {
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  if (lastFocusedElement instanceof HTMLElement) lastFocusedElement.focus();
};

const openModal = () => {
  if (!modal) return;
  lastFocusedElement = document.activeElement;
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  if (modalPanel instanceof HTMLElement) modalPanel.focus();
};

if (modal && trigger && closeBtn) {
  trigger.addEventListener('click', openModal);
  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (event) => {
    if (event.target === modal) closeModal();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });
}

if (contactForm instanceof HTMLFormElement) {
  contactForm.addEventListener('submit', (event) => {
    const honey = contactForm.querySelector('input[name="company_website"]');
    if (honey instanceof HTMLInputElement && honey.value.trim() !== '') {
      event.preventDefault();
      if (formStatus) formStatus.textContent = 'Submission blocked.';
      return;
    }

    if (!contactForm.checkValidity()) {
      event.preventDefault();
      contactForm.reportValidity();
      return;
    }

    event.preventDefault();
    if (formStatus) formStatus.textContent = 'Request submitted. The Tutoline team will contact you shortly.';
    contactForm.reset();
  });
}
