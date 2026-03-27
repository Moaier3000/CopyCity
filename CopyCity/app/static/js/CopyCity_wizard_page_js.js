const steps = document.querySelectorAll('.formStep');
const progressSteps = document.querySelectorAll('.progressStep');
const progressBar = document.getElementById('progress');
let current = 0;
 
// ── Validate all required inputs in the current step ──
function validateStep(stepIndex) {
    const inputs = steps[stepIndex].querySelectorAll('input[required]');
    let valid = true;
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.reportValidity(); // shows the browser's native "Please fill out this field"
            valid = false;
        }
    });
    return valid;
}
 
function goToStep(n) {
    if (n < 0 || n >= steps.length) return;
    // Only validate when moving forward
    if (n > current && !validateStep(current)) return;
    steps[current].classList.remove('active');
    progressSteps[current].classList.remove('active');
    current = n;
    steps[current].classList.add('active');
    progressSteps[current].classList.add('active');
    // 0% at step 0, 50% at step 1, 100% at step 2
    progressBar.style.width = (current / (steps.length - 1) * 100) + '%';
}
 
document.querySelectorAll('.nextButton').forEach(btn => {
    btn.addEventListener('click', () => goToStep(current + 1));
});
 
document.querySelectorAll('.backButton').forEach(btn => {
    btn.addEventListener('click', () => goToStep(current - 1));
});
 
progressSteps.forEach(dot => {
    dot.addEventListener('click', () => goToStep(parseInt(dot.dataset.step)));
});
 
document.getElementById('formWizard').addEventListener('submit', e => {
    e.preventDefault();
    if (!validateStep(current)) return;
    alert('Form submitted!');
});
 
// ── Toggle: switch between City name and Country name ──
const modeToggle = document.getElementById('modeToggle');
const modeTitle  = document.getElementById('modeTitle');
const dynamicInput = document.getElementById('dynamicInput');
 
modeToggle.addEventListener('change', () => {
    if (modeToggle.checked) {
        modeTitle.textContent      = 'Going of vibes';
        dynamicInput.placeholder   = ' Describe the vibe...';
    } else {
        modeTitle.textContent      = 'Have a city in mind?';
        dynamicInput.placeholder   = 'Enter a city name...';
    }
});