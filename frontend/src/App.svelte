<script>
    import Header from './components/Header.svelte';
    import Navbar from './components/Navbar.svelte';
    import ArticleGrid from './components/ArticleGrid.svelte';
    import SubmissionForm from './components/SubmissionForm.svelte';
    import Footer from './components/Footer.svelte';
</script>

<Header title="Article Viewer" />
<Navbar />

<div class="flex">
    <div class="flex-1">
        <ArticleGrid />
        <SubmissionForm />
    </div>
    <div class="w-1/3">
        <img src="/placeholder.png" alt="Placeholder" class="w-full h-auto"/>
    </div>
</div>

<Footer />
