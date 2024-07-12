async function generateComic() {
    const prompts = [];
    for (let i = 1; i <= 6; i++) {
        const prompt = document.getElementById(`prompt${i}`).value.trim();
        if (prompt === '') {
            document.getElementById('comicOutput').innerHTML = '<p>Please fill in all 6 prompts!</p>';
            return;
        }
        prompts.push({ "description": prompt, "text": "" });
    }

    const scenario = document.getElementById('storyInput').value.trim();
    const styleSelect = document.getElementById('styleSelect').value;

    if (!styleSelect) {
        document.getElementById('comicOutput').innerHTML = '<p>Please select a comic art style!</p>';
        return;
    }

    try {
        const response = await fetch('/generate_comic', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                scenario: scenario,
                prompts: prompts,
                style: styleSelect
            })
        });

        const data = await response.json();
        if (data.success) {
            document.getElementById('comicOutput').innerHTML = `<img src="${data.comic_strip_path}" alt="Generated Comic">`;
        } else {
            document.getElementById('comicOutput').innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (error) {
        document.getElementById('comicOutput').innerHTML = `<p>Error: ${error.message}</p>`;
    }
}



function setStoryInput() {
    const genreSelect = document.getElementById('genreSelect').value;
    const storyInput = document.getElementById('storyInput');

    if (genreSelect) {
        storyInput.value = `<BOS> <${genreSelect}>`;
    }
}

async function generateStory() {
    const storyInput = document.getElementById('storyInput').value.trim();
    const storyOutput = document.getElementById('storyOutput');

    if (!storyInput) {
        storyOutput.innerHTML = '<p>Please enter a story prompt!</p>';
        return;
    }

    try {
        const response = await fetch('/generate_story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt_text: storyInput })
        });

        const data = await response.json();
        if (data.success) {
            storyOutput.innerHTML = `<p>${data.story}</p>`;
        } else {
            storyOutput.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (error) {
        storyOutput.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}
