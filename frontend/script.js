 // In-memory array to store tool data
 var tools = [
    { tool: "Hammer", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", price: "$19.99" },
    { tool: "Screwdriver", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", price: "$9.99" },
    { tool: "Drill", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", price: "$49.99" }
];

// Function to display tools in the table
function displayTools() {
    var tableBody = document.querySelector("#toolTable tbody");
    tableBody.innerHTML = "";

    for (var i = 0; i < tools.length; i++) {
        var tool = tools[i];

        var row = document.createElement("tr");

        var toolCell = document.createElement("td");
        toolCell.textContent = tool.tool;
        row.appendChild(toolCell);

        var descriptionCell = document.createElement("td");
        descriptionCell.textContent = tool.description;
        row.appendChild(descriptionCell);

        var priceCell = document.createElement("td");
        priceCell.textContent = tool.price;
        row.appendChild(priceCell);

        var actionCell = document.createElement("td");
        var editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.addEventListener("click", function() {
            editTool(i);
        });
        actionCell.appendChild(editButton);

        var deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function() {
            deleteTool(i);
        });
        actionCell.appendChild(deleteButton);

        row.appendChild(actionCell);

        tableBody.appendChild(row);
    }
}

// Function to edit a tool
function editTool(index) {
    var tool = tools[index];

    // Create input elements for description and price
    var descriptionInput = document.createElement('input');
    descriptionInput.value = tool.description;

    var priceInput = document.createElement('input');
    priceInput.type = 'number';
    priceInput.value = tool.price;

    

    // Append the input elements to the body (or any other container)
    document.body.appendChild(descriptionInput);
    document.body.appendChild(priceInput);

    // Add event listeners to the input elements to update the tool's description and price
    descriptionInput.addEventListener('input', function() {
        tool.description = this.value;
        displayTools();
    });

    priceInput.addEventListener('input', function() {
        tool.price = this.value;
        displayTools();
    });
}

// Function to delete a tool
function deleteTool(index) {
    tools.splice(index, 1);
    displayTools();
}

// Initial display of tools
displayTools();