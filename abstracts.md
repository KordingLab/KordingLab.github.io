---
layout: default
title: Project Abstracts
---

# Project Abstracts

<!-- FILTERS -->
<div class="filter-container">
  <div class="filter-group">
    <label for="keyword-filter">Filter by Keyword:</label>
    <input type="text" id="keyword-filter" onkeyup="filterKeyword()" placeholder="Enter keyword..">
  </div>

  <div class="filter-group">
    <label for="pointperson-filter">Filter by Point Person:</label>
    <input type="text" id="pointperson-filter" onkeyup="filterPointPerson()" placeholder="Enter name..">
  </div>
</div>

<!-- PROJECTS LIST -->
<div class="project-list">

## Project 1: Quantum Machine Learning

**Abstract:** This project explores the intersection of quantum computing and machine learning, aiming to leverage the unique advantages of quantum systems to enhance machine learning algorithms. 

**Keywords:** Quantum Computing, Machine Learning, Quantum Algorithms

**Point Person:** Jane Doe

**Skill Level:** Suitable for a graduate student with understanding of Quantum Computing and Machine Learning.

## Project 2: Primate Facial Recognition

**Abstract:** This project aims to develop a computer vision system capable of recognizing and distinguishing different primates based on facial features. It involves designing a deep learning model trained on a dataset of primate images, potentially gathered from zoos, wildlife documentaries, and field researchers. The goal is not only to distinguish between different species, but also to recognize individuals within a species. Such technology could be immensely beneficial in primatology research, aiding in individual tracking, behavioral studies, and conservation efforts.

**Keywords:** Computer Vision, Primatology, Facial Recognition, Deep Learning

**Point Person:** John Doe

**Skill Level:** This project is ideal for a senior with knowledge of Python, Machine Learning, and a basic understanding of Computer Vision

</div>

<!-- FILTER SCRIPTS -->
<script>
  // Keyword Filter
  function filterKeyword() {
    let input, filter, projects, keywords, i, txtValue;
    input = document.getElementById('keyword-filter');
    filter = input.value.toUpperCase();
    projects = document.getElementsByClassName('project-list');
    
    for (i = 0; i < projects.length; i++) {
      keywords = projects[i].getElementsByClassName('keywords')[0];
      txtValue = keywords.textContent || keywords.innerText;
      
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        projects[i].style.display = "";
      } else {
        projects[i].style.display = "none";
      }
    }
  }
  
  // Point Person Filter
  function filterPointPerson() {
    let input, filter, projects, pointPersons, i, txtValue;
    input = document.getElementById('pointperson-filter');
    filter = input.value.toUpperCase();
    projects = document.getElementsByClassName('project-list');
    
    for (i = 0; i < projects.length; i++) {
      pointPersons = projects[i].getElementsByClassName('pointperson')[0];
      txtValue = pointPersons.textContent || pointPersons.innerText;
      
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        projects[i].style.display = "";
      } else {
        projects[i].style.display = "none";
      }
    }
  }
</script>
