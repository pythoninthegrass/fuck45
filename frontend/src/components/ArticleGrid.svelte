<script>
    import { onMount } from 'svelte';
    let articles = [];
    let page = 1;

    async function fetchArticles() {
        const res = await fetch(`/api/articles/?page=${page}`);
        articles = await res.json();
    }

    function nextPage() {
        page++;
        fetchArticles();
    }

    function prevPage() {
        if (page > 1) {
            page--;
            fetchArticles();
        }
    }

    onMount(fetchArticles);
</script>

<div class="grid grid-cols-3 gap-4 p-4">
    {#each articles as article}
        <div class="border p-4">
            <a href={article.url} target="_blank">
                {article.title.length > 50 ? article.title.substring(0, 50) + '...' : article.title}
            </a>
        </div>
    {/each}
</div>
<div class="flex justify-between p-4">
    <button on:click={prevPage} class="p-2 bg-gray-300">{'<'}</button>
    <button on:click={nextPage} class="p-2 bg-gray-300">{'>'}</button>
</div>
