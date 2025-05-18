document.addEventListener('DOMContentLoaded', function() {
    // Create and initialize the binary background effect
    initBinaryBackground();
    
    // Add focus styling to form inputs
    addInputFocusStyling();
    
    // Add digital hover effects to alphabet letters
    addAlphabetLetterEffects();
    
    // Add digital matrix effects
    addDigitalMatrixEffects();
});

/**
 * Creates the dynamic binary background
 */
function initBinaryBackground() {
    const binaryBackground = document.getElementById('binaryBackground');
    if (!binaryBackground) return;
    
    const characters = '01';
    const columns = Math.floor(window.innerWidth / 40); // More columns for denser appearance
    
    for (let i = 0; i < columns; i++) {
        const column = document.createElement('div');
        column.classList.add('binary-column');
        
        // Randomize position and animation speed
        column.style.left = `${i * 40 + Math.random() * 10}px`;
        column.style.top = `${Math.random() * -1000}px`;
        column.style.animationDuration = `${Math.random() * 30 + 15}s`;
        column.style.opacity = Math.random() * 0.4 + 0.2; // Varying opacity
        binaryBackground.appendChild(column);
        
        // Generate binary content with varying patterns
        let binaryString = '';
        const length = Math.floor(Math.random() * 20) + 15;
        
        for (let j = 0; j < length; j++) {
            // Create occasional small patterns instead of pure random
            if (Math.random() > 0.7) {
                // Repeat patterns
                const pattern = Math.random() > 0.5 ? '10' : '01';
                binaryString += pattern.repeat(Math.floor(Math.random() * 2) + 1) + '<br>';
            } else {
                // Random characters
                binaryString += characters.charAt(Math.floor(Math.random() * characters.length)) + '<br>';
            }
        }
        
        column.innerHTML = binaryString;
    }
    
    // Animation keyframes
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes fall {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(${window.innerHeight + 500}px); }
        }
    `;
    document.head.appendChild(style);

    // Add occasional new columns for dynamic effect
    setInterval(() => {
        if (binaryBackground.children.length > 50) return; // Limit max columns
        
        const newColumn = document.createElement('div');
        newColumn.classList.add('binary-column');
        newColumn.style.left = `${Math.random() * window.innerWidth}px`;
        newColumn.style.top = `-500px`;
        newColumn.style.animationDuration = `${Math.random() * 30 + 20}s`;
        newColumn.style.opacity = Math.random() * 0.4 + 0.2;
        
        let newBinaryString = '';
        const newLength = Math.floor(Math.random() * 15) + 10;
        
        for (let j = 0; j < newLength; j++) {
            newBinaryString += characters.charAt(Math.floor(Math.random() * characters.length)) + '<br>';
        }
        
        newColumn.innerHTML = newBinaryString;
        binaryBackground.appendChild(newColumn);
        
        // Remove old columns to prevent excessive DOM nodes
        if (binaryBackground.children.length > 80) {
            binaryBackground.removeChild(binaryBackground.children[0]);
        }
    }, 5000);
}

/**
 * Adds focus styling to form inputs
 */
function addInputFocusStyling() {
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.transition = 'all 0.2s ease';
        });
    });
}

/**
 * Adds interactive effects to alphabet letters
 */
function addAlphabetLetterEffects() {
    const alphabetLetters = document.querySelectorAll('.alphabet-letter');
    
    alphabetLetters.forEach(letter => {
        // Add subtle highlight effect on hover
        letter.addEventListener('mouseover', function() {
            // Highlight the matching letter in the other row
            const index = Array.from(letter.parentNode.children).indexOf(letter) - 1; // -1 to account for the <strong> element
            
            if (index >= 0) {
                const rows = letter.parentNode.parentNode.querySelectorAll('.alphabet-row');
                if (rows.length >= 2) {
                    // Find the corresponding letter in the other row
                    const otherRow = letter.parentNode === rows[0] ? rows[1] : rows[0];
                    const matchingLetter = otherRow.children[index + 1]; // +1 to account for the <strong> element
                    
                    if (matchingLetter) {
                        // Add a temporary highlight class
                        matchingLetter.classList.add('highlight');
                        setTimeout(() => {
                            matchingLetter.classList.remove('highlight');
                        }, 500);
                    }
                }
            }
        });
    });
}

/**
 * Adds additional digital matrix effects to the UI
 */
function addDigitalMatrixEffects() {
    // Add digital flicker effect to binary badges
    const binaryBadges = document.querySelectorAll('.binary-badge');
    binaryBadges.forEach(badge => {
        setInterval(() => {
            // Randomly change some digits in the binary string
            const content = badge.textContent;
            let newContent = '';
            for (let i = 0; i < content.length; i++) {
                if (Math.random() > 0.9 && (content[i] === '0' || content[i] === '1')) {
                    newContent += content[i] === '0' ? '1' : '0';
                } else {
                    newContent += content[i];
                }
            }
            badge.textContent = newContent;
        }, 2000);
    });

    // Periodically add binary "glitch" effects
    setInterval(() => {
        // Create a temporary "glitch" element
        const glitch = document.createElement('div');
        glitch.style.position = 'fixed';
        glitch.style.left = `${Math.random() * window.innerWidth}px`;
        glitch.style.top = `${Math.random() * window.innerHeight}px`;
        glitch.style.fontFamily = 'monospace';
        glitch.style.fontSize = '12px';
        glitch.style.color = 'rgba(59, 130, 246, 0.3)';
        glitch.style.pointerEvents = 'none';
        glitch.style.zIndex = '9999';
        glitch.style.transition = 'opacity 1s';
        
        // Generate a random string of 0s and 1s
        let binaryGlitch = '';
        const length = Math.floor(Math.random() * 8) + 4;
        for (let i = 0; i < length; i++) {
            binaryGlitch += Math.random() > 0.5 ? '1' : '0';
        }
        glitch.textContent = binaryGlitch;
        
        // Add to DOM temporarily
        document.body.appendChild(glitch);
        
        // Fade out and remove
        setTimeout(() => {
            glitch.style.opacity = '0';
        }, 500);
        setTimeout(() => {
            document.body.removeChild(glitch);
        }, 1500);
    }, 5000);
}