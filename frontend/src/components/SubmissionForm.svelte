<script>
    let url = '';
    let message = '';

    async function submitUrl() {
        const res = await fetch('/api/submissions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });

        if (res.ok) {
            message = 'Submission successful!';
        } else {
            message = 'Error submitting the URL.';
        }

        url = '';
    }
</script>

<div class="p-4">
    <input type="url" bind:value={url} placeholder="Enter article URL" class="p-2 border"/>
    <button on:click={submitUrl} class="p-2 bg-blue-500 text-white">Submit</button>
    {#if message}
        <p>{message}</p>
    {/if}
</div>
