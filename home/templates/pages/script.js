const line = document.querySelector('.hover-line');
  const links = document.querySelectorAll('.custom-h1-style');

  links.forEach((link) => {
    link.addEventListener('mouseover', () => {
      const linkPosition = link.getBoundingClientRect();
      const lineWidth = linkPosition.width / 2;
      line.style.width = `${lineWidth * 2+8}px`;
      line.style.left = `${linkPosition.left - lineWidth+25}px`; // Adjusted left position
      line.style.top = 0;
    });

    link.addEventListener('mouseout', () => {
      line.style.width = 0;
    });
  });
  document.addEventListener("DOMContentLoaded", function() {
        const sortingOptions = document.getElementById("sorting-options");
        const carList = document.getElementById("car-list");

        sortingOptions.addEventListener("change", function() {
            const selectedOption = sortingOptions.value;
            const carContainers = document.querySelectorAll(".car-container");
            const carArray = Array.from(carContainers);

            if (selectedOption === "price-asc") {
                carArray.sort((a, b) => {
                    const priceA = parseInt(a.dataset.price);
                    const priceB = parseInt(b.dataset.price);
                    return priceA - priceB;
                });
            } else if (selectedOption === "price-desc") {
                carArray.sort((a, b) => {
                    const priceA = parseInt(a.dataset.price);
                    const priceB = parseInt(b.dataset.price);
                    return priceB - priceA;
                });
            } else if (selectedOption === "year-asc") {
                carArray.sort((a, b) => {
                    const yearA = parseInt(a.dataset.year);
                    const yearB = parseInt(b.dataset.year);
                    return yearA - yearB;
                });
            } else if (selectedOption === "year-desc") {
                carArray.sort((a, b) => {
                    const yearA = parseInt(a.dataset.year);
                    const yearB = parseInt(b.dataset.year);
                    return yearB - yearA;
                });
            }

            // Clear the current car list
            carList.innerHTML = '';

            // Slide in the sorted car containers
            carArray.forEach((container, index) => {
                container.style.transform = `translateX(${index * 25}%)`;
                carList.appendChild(container);
                // Trigger reflow for the transition to work
                container.getBoundingClientRect();
                container.style.transform = 'translateX(0)';
            });
        });
    });

  function filterCarsByType() {
        var selectedType = document.getElementById("type-filter").value;
        var carContainers = document.getElementsByClassName("car-container");
        var uniqueTypes = [];

        for (var i = 0; i < carContainers.length; i++) {
            var carType = carContainers[i].getAttribute("data-type");

            // Initially show all cars
            carContainers[i].style.display = "block";

            // Hide cars that don't match the selected type
            if (selectedType !== "all" && carType !== selectedType) {
                carContainers[i].style.display = "none";
            }

            // Keep track of unique types with visible cars
            if (carContainers[i].style.display === "block" && uniqueTypes.indexOf(carType) === -1) {
                uniqueTypes.push(carType);
            }
        }

        // Hide type names that have no visible cars
        var typeOptions = document.getElementById("type-filter").getElementsByTagName("option");
        for (var i = 0; i < typeOptions.length; i++) {
            var typeValue = typeOptions[i].value;
            if (typeValue !== "all" && uniqueTypes.indexOf(typeValue) === -1) {
                typeOptions[i].style.display = "none";
            } else {
                typeOptions[i].style.display = "block";
            }
        }
    }
    document.addEventListener("DOMContentLoaded", function () {
    const carList = document.getElementById("car-list");
    const showMoreButton = document.getElementById("show-more");
    const cars = carList.querySelectorAll(".card1");
    const itemsToShow = 8; // Number of items to show initially
    let visibleItems = itemsToShow;

    // Function to show or hide car listings with animation
    function toggleCarList() {
        cars.forEach((car, index) => {
            if (index < visibleItems) {
                car.style.display = "block";
                setTimeout(() => {
                    car.style.opacity = 1;
                    car.style.transform = "translateX(0)";
                }, 100 * index); // Delay the animation for each item
            } else {
                car.style.opacity = 0;
                car.style.transform = "translateX(-20px)";
                car.style.display = "none";
            }
        });

        if (visibleItems < cars.length) {
            showMoreButton.textContent = "Show More";
            showMoreButton.style.display = "block"; // Ensure the button is visible
        } else {
            showMoreButton.style.display = "none"; // Hide the button if not enough cars to show
        }

    }

    // Initial setup
    toggleCarList();

    // Event listener for "Show More/Show Less" button
    showMoreButton.addEventListener("click", function () {
        if (visibleItems === itemsToShow) {
            visibleItems = cars.length; // Show all cars
        } else {
            visibleItems = itemsToShow; // Show initial number of cars
        }
        toggleCarList();
    });

    // Event listener for sorting options
    const sortingOptions = document.getElementById("sorting-options");
    sortingOptions.addEventListener("change", function () {
        const selectedOption = sortingOptions.value;

        // Send selected sorting option and brand filter to the Django view using AJAX
        filterAndSortCars();
    });

    // Event listener for brand filter
    const brandFilter = document.getElementById("brand-filter");
    brandFilter.addEventListener("change", function () {
        const selectedBrand = brandFilter.value;

        // Send selected sorting option and brand filter to the Django view using AJAX
        filterAndSortCars();
    });
});
  $(document).ready(function () {
        $("#openDialogButton5").click(function () { // Use the unique ID for the button
            $("#dialogBox5").fadeIn(); // Use the unique ID for the dialog box
            $("#overlay5").fadeIn(); // Use the unique ID for the overlay
        });

        $("#closeDialogButton5").click(function () { // Use the unique ID for the button
            $("#dialogBox5").fadeOut(); // Use the unique ID for the dialog box
            $("#overlay5").fadeOut(); // Use the unique ID for the overlay
        });
    });

  if (document.getElementById('state1')) {
    const countUp = new CountUp('state1', document.getElementById("state1").getAttribute("countTo"));
    if (!countUp.error) {
      countUp.start();
    } else {
      console.error(countUp.error);
    }
  }
  if (document.getElementById('state2')) {
    const countUp1 = new CountUp('state2', document.getElementById("state2").getAttribute("countTo"));
    if (!countUp1.error) {
      countUp1.start();
    } else {
      console.error(countUp1.error);
    }
  }
  if (document.getElementById('state3')) {
    const countUp2 = new CountUp('state3', document.getElementById("state3").getAttribute("countTo"));
    if (!countUp2.error) {
      countUp2.start();
    } else {
      console.error(countUp2.error);
    };
  }