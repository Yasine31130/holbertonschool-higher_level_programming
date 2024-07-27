document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const myList = document.querySelector('.my_list');
  // Select class with '.' !

  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});
