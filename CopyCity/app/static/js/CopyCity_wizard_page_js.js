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
    
    // Hide the current form step
    steps[current].classList.remove('active');
    
    // Update the current index
    current = n;
    
    // Show the new form step
    steps[current].classList.add('active');
    
    // Update the progress steps (dots)
    progressSteps.forEach((dot, index) => {
        if (index <= current) {
            // Add 'active' class to current and all previous steps
            dot.classList.add('active');
        } else {
            // Remove 'active' class from future steps
            dot.classList.remove('active');
        }
    });
    
    // Update the progress bar fill line (0% at step 0, 50% at step 1, 100% at step 2)
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
document.getElementById('formWizard').addEventListener('submit', async function(event) {
    // Prevent the default form submission (which would reload the page)
    event.preventDefault(); 

    // 1. Extract values from the form inputs
    const city = document.getElementById('dynamicInput').value;
    const budget = document.querySelector('input[placeholder="ex. 123$"]').value;
    const days = document.querySelector('input[placeholder="Days of stay"]').value;
    const interests = document.querySelector('input[placeholder="Interests (required)"]').value;

    // 2. Format the payload to match what your Python script expects
    const payload = {
        city: city,
        budget: Number(budget), // Converting to numbers for cleaner data
        days: Number(days),
        interests: interests
    };

    console.log("Sending data to backend:", payload);

    // 3. Send the POST request
    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 4. Parse the JSON returned by Python/Ollama
        const recommendations = await response.json();
        
        console.log("Success! Here are the cities:", recommendations);
        
        window.location.href = '/map';
    } catch (error) {
        console.error("Failed to fetch recommendations:", error);
    }
});


const modeToggle = document.getElementById('modeToggle');
const modeTitle  = document.getElementById('modeTitle');
const dynamicInput = document.getElementById('dynamicInput');
 
modeToggle.addEventListener('change', () => {
    if (modeToggle.checked) {
        modeTitle.textContent      = 'Have a city in mind?';
        dynamicInput.placeholder   = ' Enter a city name...';
    } else {
        modeTitle.textContent      = 'What is the vibe?';
        dynamicInput.placeholder   = 'Describe the surroundings...';
    }
});