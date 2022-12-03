<script>
  import { onMount } from 'svelte';
  import Wall from './Wall.svelte';

  let stickyNotesList = [];
  let currentText = '';

  onMount(async() => {
    await getStickyNotes();
  })

  async function getStickyNotes() {
    let response = await fetch('./notes', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    let result = await response.json();
    stickyNotesList = result.sticky_notes;
  }

  async function createStickyNote() {
    let response = await fetch('./notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: currentText
      })
    });

    response.status === 200 && await getStickyNotes();
    currentText = '';
  }

  async function deleteStickyNote(event) {
    const index = event.detail.index;

    let response = await fetch(`./notes/${index}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    response.status === 200 && await getStickyNotes();
  }
</script>

<form on:submit|preventDefault={createStickyNote}>
  <div>
    Enter your note...
    <input bind:value={currentText} type="text" id="stickyText"/>
  </div>
  <button type="submit">Sticky Note +</button>
</form>

<Wall bind:stickyNotesList={stickyNotesList} on:remove={deleteStickyNote} />
