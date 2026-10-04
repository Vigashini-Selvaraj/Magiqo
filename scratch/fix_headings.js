const fs = require('fs');

const indexHtmlPath = 'c:/Users/vigas/Desktop/magiqo/index.html';
let indexContent = fs.readFileSync(indexHtmlPath, 'utf8');

// Replace <div class="section-title"...>...</div> with <h2>...</h2> and strip spans inside them.
// Actually, let's just do a regex replace for the specific blocks we know.

// Helper to strip specific spans inside a string
function stripSpans(html) {
    return html.replace(/<span[^>]*>(.*?)<\/span>/gi, '$1').replace(/\s+/g, ' ').trim();
}

indexContent = indexContent.replace(/<div class="section-title"[^>]*>([\s\S]*?)<\/div>/gi, (match, p1) => {
    let innerText = stripSpans(p1);
    return `<h2 class="section-title" style="font-family: var(--font-magic); text-align: center; font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem;">${innerText}</h2>`;
});

// Also fix the hero h1 which might have inline colors
indexContent = indexContent.replace(/<h1[^>]*>([\s\S]*?)<\/h1>/gi, (match, p1) => {
    let innerText = stripSpans(p1);
    // ensure no inline color on h1
    return `<h1 style="font-size: clamp(3rem, 5vw + 1rem, 5.5rem); line-height: 1.1; margin-bottom: 1.5rem; font-family: var(--font-magic, 'Berkshire Swash'); font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">${innerText}</h1>`;
});

fs.writeFileSync(indexHtmlPath, indexContent);
console.log('Fixed index.html headings.');
