<script>
  import StickyNote from './StickyNote.svelte';
  export let stickyNotesList = [];
</script>

{#each stickyNotesList as stickyNote (stickyNote.index)}
  <StickyNote index={stickyNote.index} on:remove>
    <div slot='text' data-index={stickyNote.index}>{stickyNote.text}</div>
  </StickyNote>
{/each}
