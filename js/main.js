// js/main.js
document.addEventListener('DOMContentLoaded', function() {
    loadUserStories();
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./js/serviceWorker.js').then(function() {
            console.log('Service Worker Registered');
        });
    }
});

function loadUserStories() {
    const userStories = KanbanService.getUserStories();
    const backlog = document.querySelector('#backlog .story-list');
    const inProgress = document.querySelector('#in-progress .story-list');
    const done = document.querySelector('#done .story-list');

    backlog.innerHTML = '';
    inProgress.innerHTML = '';
    done.innerHTML = '';

    userStories.forEach(story => {
        const li = document.createElement('li');
        li.setAttribute('draggable', 'true');
        li.setAttribute('data-id', story.id);
        li.setAttribute('ondragstart', 'drag(event)');
        li.innerHTML = `<strong>${story.title}</strong>`;

        if (story.status === 'backlog') {
            backlog.appendChild(li);
        } else if (story.status === 'in-progress') {
            inProgress.appendChild(li);
        } else if (story.status === 'done') {
            done.appendChild(li);
        }
    });
}

function addUserStory() {
    const title = document.getElementById('user-story-title').value;
    if (title) {
        const userStory = { id: Date.now(), title, status: 'backlog' };
        KanbanService.addUserStory(userStory);
        loadUserStories();
        document.getElementById('user-story-title').value = '';
    } else {
        alert('User story title is required');
    }
}

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData('text', event.target.getAttribute('data-id'));
}

function drop(event) {
    event.preventDefault();
    const id = event.dataTransfer.getData('text');
    const status = event.target.getAttribute('data-status');
    if (status) {
        KanbanService.updateUserStoryStatus(Number(id), status);
        loadUserStories();
    }
}

document.querySelectorAll('.story-list').forEach(list => {
    list.addEventListener('dragover', allowDrop);
    list.addEventListener('drop', drop);
});
