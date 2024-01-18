function checkOther(selectElement) {
    const otherInputId = selectElement.id.startsWith('country') ? 'other_country' : 'other_nationality';
    const otherInput = document.getElementById(otherInputId);

    if (selectElement.value.toLowerCase() === '1') {
        otherInput.style.display = 'block';
    } else {
        otherInput.style.display = 'none';
        otherInput.value = '';
    }
}

function validateForm() {
    console.log('Form submitted successfully!');
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const country = document.getElementById('country').value;
    const otherCountry = document.getElementById('other_country').value;
    const nationality = document.getElementById('nationality').value;
    const otherNationality = document.getElementById('other_nationality').value;
    const fullName = document.getElementById('fullName').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    const emailError = document.getElementById('emailError');
    const mobileError = document.getElementById('mobileError');
    const countryError = document.getElementById('countryError');
    const nationalityError = document.getElementById('nationalityError');
    const fullNameError = document.getElementById('fullNameError');
    const passwordError = document.getElementById('passwordError');
    const confirmPasswordError = document.getElementById('confirmPasswordError');

    emailError.innerHTML = '';
    mobileError.innerHTML = '';
    countryError.innerHTML = '';
    nationalityError.innerHTML = '';
    fullNameError.innerHTML = '';
    passwordError.innerHTML = '';
    confirmPasswordError.innerHTML = '';

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        emailError.innerHTML = 'Invalid email address';
        return false;
    }

    const mobileRegex = /^\d{1,}$/;
    if (!mobileRegex.test(mobile)) {
        mobileError.innerHTML = 'Invalid mobile number';
        return false;
    }

    if (country.toLowerCase() === 'other' && !otherCountry.trim()) {
        countryError.innerHTML = 'Please enter the country';
        return false;
    }

    if (nationality.toLowerCase() === 'other' && !otherNationality.trim()) {
        nationalityError.innerHTML = 'Please enter the nationality';
        return false;
    }

    if (!fullName.trim()) {
        fullNameError.innerHTML = 'Please enter your full name';
        return false;
    }

    if (password.length < 8) {
        passwordError.innerHTML = 'Password must be at least 8 characters long';
        return false;
    }

    if (confirmPassword !== password) {
        confirmPasswordError.innerHTML = 'Passwords do not match';
        return false;
    }

    return true;
}