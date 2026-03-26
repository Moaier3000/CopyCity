const steps = document.querySelectorAll(".formStep")
const nextButton = document.querySelectorAll(".nextButton")
const backButton = document.querySelectorAll(".backButton")
const progress = document.querySelector("#progress")
const progressStep = document.querySelectorAll(".progressStepButton")
const form = document.querySelector("#formWizard")

let formStepIndex = 0;

function validateStep(stepIndex){
    const step = steps[stepIndex]
    const requiredInputs = step.querySelectorAll("input[required]")
    let valid = true;

    requiredInputs.forEach(input => {
        if (!input.value.trim()){
            input.style.borderColor = "#f44336"
            valid = false;
        } else {
            input.style.borderColor = ""
        }
    })

    let errorDiv = step.querySelector("#formError")

    if (!valid){
        if(!errorDiv){
            errorDiv = document.createElement("div")
            errorDiv.id = "formError"
            errorDiv.textContent = "Please fill out all required fields."
            errorDiv.style.color = "#f44336"
            errorDiv.style.marginBottom = "10px"
            step.insertBefore(errorDiv, step.firstChild)
        }
    } else if (errorDiv){
        errorDiv.remove()
    }

    return valid
}

nextButton.forEach(button =>{
    button.addEventListener("click", () =>{
        if (validateStep(formStepIndex)) {
            if (formStepIndex < steps.length - 1) {
                formStepIndex++
            }
            updateFormSteps()
            updateProgressBar()
        }
    })
})

backButton.forEach(button =>{
    button.addEventListener("click", () =>{
        if (formStepIndex > 0) {
            formStepIndex--
        }
        updateFormSteps()
        updateProgressBar()
    })
})

progressStep.forEach(button => {
    button.addEventListener("click", () => {
        const step = parseInt(button.getAttribute("data-step"))
        formStepIndex = step
        updateFormSteps()
        updateProgressBar()
    })
})

form.addEventListener("submit", function(e) {
    if (!validateStep(formStepIndex)){
        e.preventDefault()
    }
})

function updateFormSteps(){
    steps.forEach((step, index) => {
        step.classList.toggle("active", index === formStepIndex)
    })
}

function updateProgressBar(){
    progressStep.forEach((step ,index) => {
        step.classList.toggle("active", index <= formStepIndex)
    })

    progress.style.width =
    (formStepIndex / (progressStep.length - 1)) * 100 + "%"
}

const toggle = document.getElementById("modeToggle");
const title = document.getElementById("modeTitle");
const input = document.getElementById("dynamicInput");

toggle.addEventListener("change", () => {
    if (toggle.checked) {
        title.textContent = "City description";
        input.placeholder = "Enter a vibe (e.g. beach, nightlife, quiet...)";
    } else {
        title.textContent = "City name";
        input.placeholder = "Enter a city name...";
    }

    input.value = ""; // optional: clear input on switch
});

updateFormSteps()