// Function to toggle visibility of lessons within a module
function toggleLessons(lessonId) {
    const lesson = document.getElementById(lessonId);
    if (lesson.style.display === "block") {
        lesson.style.display = "none";
    } else {
        lesson.style.display = "block";
    }
}

// Function to toggle visibility of the entire module
function toggleModule(moduleId) {
    const module = document.getElementById(moduleId);
    if (module.style.display === "block") {
        module.style.display = "none";
    } else {
        module.style.display = "block";
    }
}
