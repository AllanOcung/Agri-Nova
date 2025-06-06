// Set the button text to the first farm in the list on page load
document.addEventListener("DOMContentLoaded", function () {
  var farmList = document.querySelectorAll("#farmList .farm-option");
  var selectedFarm = document.getElementById("selectedFarm");
  if (farmList.length > 0) {
    selectedFarm.textContent = farmList[0].textContent;
  }
  // Update button text when a farm is selected
  farmList.forEach(function (btn) {
    btn.onclick = function () {
      selectedFarm.textContent = this.textContent;
      document.getElementById("farmModal").classList.remove("show");
    };
  });
  // Modal open/close logic
  document.getElementById("openFarmModal").onclick = function () {
    document.getElementById("farmModal").classList.add("show");
  };
  document.getElementById("closeFarmModal").onclick = function () {
    document.getElementById("farmModal").classList.remove("show");
  };
  window.onclick = function (event) {
    const modal = document.getElementById("farmModal");
    if (event.target === modal) {
      modal.classList.remove("show");
    }
  };
});

// document.getElementById('openFarmModal').onclick = function() {
//   document.getElementById('farmModal').classList.add('show');
// };
// document.getElementById('closeFarmModal').onclick = function() {
//   document.getElementById('farmModal').classList.remove('show');
// };
// // Optional: Close modal when clicking outside content
// window.onclick = function(event) {
//   const modal = document.getElementById('farmModal');
//   if (event.target === modal) {
//     modal.classList.remove('show');
//   }
// };
// // Optional: Set selected farm text on button
// document.querySelectorAll('.farm-option').forEach(function(btn) {
//   btn.onclick = function() {
//     document.getElementById('openFarmModal').innerHTML = this.textContent + ' <i class="fas fa-chevron-down"></i>';
//     document.getElementById('farmModal').classList.remove('show');
//   };
// });
