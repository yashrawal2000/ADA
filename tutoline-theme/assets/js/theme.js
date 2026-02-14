'use strict';

const modal = document.getElementById('previewModal');
const trigger = document.getElementById('previewTrigger');
const closeBtn = document.getElementById('closeModal');
const modalPanel = document.querySelector('.modal-panel');
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
