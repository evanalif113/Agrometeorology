# Greenhouse Heatmap Visualization

This project reads a CSV file containing sensor data, processes the data, and creates a heatmap visualization using Altair.

## Prerequisites

- Python 3.x
- Pandas
- Altair
- VegaFusion

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas altair vegafusion
    ```

## Usage

1. Update the `file_path` variable in [Greenhouse_Heatmap.ipynb](http://_vscodecontentref_/1) to point to your CSV file containing the sensor data.

2. Run the Jupyter Notebook:
    ```sh
    jupyter notebook Greenhouse_Heatmap.ipynb
    ```

3. The notebook will read the CSV file, process the data, and display a heatmap visualization.

## Data Processing

- Reads the CSV file with a semicolon delimiter.
- Converts the 'created_at' column to datetime format.
- Converts the 'suhu' and 'kelembaban' columns to numeric format.
- Extracts the day and hour from the 'created_at' column into 'waktu' and 'jam' columns, respectively.

## Visualization

- Creates a heatmap using Altair's `mark_rect`.
- Encodes the x-axis with hours ('jam'), y-axis with days ('waktu'), and color with the maximum temperature ('max(suhu)').
- Adds tooltips for 'waktu', 'jam', and 'max(suhu)'.
- Configures the view and axis properties for better visualization.
- Displays the heatmap chart.

## License

This project is licensed under the MIT License.
