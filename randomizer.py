import json
import random
import os
from datetime import datetime
import uuid


# Constants for the limits
HORIZONTAL_SCALE_MIN = 1.0
HORIZONTAL_SCALE_MAX = 8192.0
ZOOM_MIN = 0.00005
EXPONENT_MIN = 0.01562
EXPONENT_MAX = 64.0
MULTIPLIER_MIN = 0.00005
OPACITY_MIN = 0.0
OPACITY_MAX = 1.0
ZOOM_MAX = 50  
MULTIPLIER_MAX = 100 
CLIFF_HEIGHT_MAX = 100
OCTAVES_MIN = 1
OCTAVES_MAX = 20
OFFSET_MAX = 30
CELL_FRACTURE_HEIGHT_MAX = 50.0
CELL_FRACTURE_ZOOM_MAX = 50.0
CELL_PERCENT_SIZE_MAX = 1.0

def generate_random_number(min_value, max_value, is_int=False, decimal_places=3):
    if is_int:
        return random.randint(min_value, max_value)
    else:
        if max_value is float('inf'):
            max_value = 1e6  # Adjust this number as needed
        value = random.uniform(min_value, max_value)
        return round(value, random.randint(0, decimal_places))

def randomize_values(data):
    for key, value in data.items():
        if isinstance(value, dict):
            randomize_values(value)
        elif isinstance(value, list):
            for item in value:
                randomize_values(item)
        elif isinstance(value, bool):
            data[key] = random.choice([True, False])
        elif isinstance(value, str):
            if key == 'style' and value in style_options:
                data[key] = random.choice(style_options)
            elif key == 'function' and value in function_options:
                data[key] = random.choice(function_options)
        elif isinstance(value, (int, float)):
            if key == 'horizontalScale':
                data[key] = generate_random_number(HORIZONTAL_SCALE_MIN, HORIZONTAL_SCALE_MAX)
            elif key == 'zoom':
                data[key] = generate_random_number(ZOOM_MIN, ZOOM_MAX)
            elif key == 'exponent':
                data[key] = generate_random_number(EXPONENT_MIN, EXPONENT_MAX)
            elif key == 'multiplier':
                data[key] = generate_random_number(MULTIPLIER_MIN, MULTIPLIER_MAX)
            elif key == 'opacity':
                data[key] = generate_random_number(OPACITY_MIN, OPACITY_MAX)
            elif key == 'seed':
                data[key] = generate_random_number(0, 200, is_int=True)
            elif key in ['cellularZoom', 'cellularFrequency', 'offsetX', 'offsetY', 'offsetZ']:
                data[key] = generate_random_number(0.005, OFFSET_MAX)
            elif key == 'octaves':
                data[key] = generate_random_number(OCTAVES_MIN, OCTAVES_MAX, is_int=True)
            elif key in ['cliffHeightMax', 'cliffHeightMin', 'cellFractureHeight', 'cellFractureShuffle']:
                data[key] = generate_random_number(0.0, CLIFF_HEIGHT_MAX)
            elif key == 'cellFractureZoom':
                data[key] = generate_random_number(0.001, CELL_FRACTURE_ZOOM_MAX)
            elif key == 'cellPercentSize':
                data[key] = generate_random_number(0.0, CELL_PERCENT_SIZE_MAX)

def randomize_json_and_save_with_random_name(save_path, json_data):
    randomize_values(json_data)
    random_file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4()}.json"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    complete_file_path = os.path.join(save_path, random_file_name)
    with open(complete_file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
    return complete_file_path

def select_template():
    print("Select a template:")
    print("1: Basic Template")
    print("2: Cliff and Cells")
    print("3: Cliffs")
    print("4: Cells")
    choice = input("Enter your choice (1, 2, 3 or 4): ").strip()

    if choice == '1':
        return sample_json1 
    elif choice == '2':
        return sample_json2  
    elif choice == '3':
        return sample_json3  
    elif choice == '4':
        return sample_json4      
    else:
        print("Invalid choice. Defaulting to original template.")
        return sample_json1

sample_json1 = {
    "interpolator": {
        "function": "BILINEAR_STARCAST_3",
        "horizontalScale": 5.0
    },
    "seed": 530530,
    "composite": [
        {
            "seed": 5346,
            "style": {
                "style": "NOWHERE",
                "zoom": 1.7,
                "fracture": {
                    "style": "STATIC",
                    "zoom": 0.8,
                    "exponent": 1.2,
                    "multiplier": 55.0
                }
            },
            "exponent": 4.0,
            "negative": True
        },
        {
            "seed": 1714,
            "style": {
                "style": "IRIS_THICK",
                "zoom": 0.6,
                "exponent": 0.7,
                "fracture": {
                    "style": "STATIC",
                    "zoom": 0.8,
                    "exponent": 0.7,
                    "multiplier": 50.0
                }
            },
            "negative": True,
            "opacity": 0.1
        }
    ]
}

sample_json2 = {
  "interpolator": {
    "function": "BILINEAR_STARCAST_9",
    "horizontalScale": 12
  },
  "seed": 7246661,
  "composite": [
    {
      "style": {
        "style": "GLOB",
        "zoom": 1.3,
        "exponent": 0.7,
        "fracture": {
          "style": "NOWHERE",
          "zoom": 0.1,
          "cellularZoom": 0,
          "axialFracturing": True,
          "cellularFrequency": 0,
          "exponent": 0.01562,
          "multiplier": 5
        }
      },
      "negative": True,
      "seed": 10056
    }
  ],
  "cliffHeightMax": 80,
  "cliffHeightMin": 35,
  "cliffHeightGenerator": {
    "seed": 2348,
    "bezier": True,
    "enabled": True,
    "exponent": 0.0,
    "style": {"style": "CELLULAR_HEIGHT"},
    "zoom": 0.4,
    "fracture": [{
      "bezier": True,
      "enabled": True,
      "exponent": 0,
      "zoom": 0.0001,
      "style": {
        "style": "BIOCTAVE_FRACTAL_BILLOW_PERLIN",
        "axialFracturing": True,
        "cellularFrequency": 0.0,
        "cellularZoom": 0.0,
        "exponent": 0.01562,
        "multiplier": 0.00001,
        "zoom": 0.0001
        },
      "sinCentered": True,
      "negative": True,
      "seed": 0,
      "parametric": True,
      "octaves": 1,
      "offsetX": 0.0,
      "offsetY": 0.0,
      "offsetZ": 0.0,
      "opacity": 0.0
    }]
  },
  "cellFractureHeight": 0.0,
  "cellFractureShuffle": 0.0,
  "cellFractureZoom": 1000,
  "cellPercentSize": 0.0,
  "multiplicitive": False,
  "offsetX": 0.0,
  "offsetZ": 0.0,
  "opacity": 0.0,
  "zoom": 0.01
}

sample_json3 = {
    "interpolator": {
        "function": "HERMITE_STARCAST_12",
        "horizontalScale": 1898.256
    },
    "seed": 30,
    "composite": [
        {
            "style": {
                "style": "CELLULAR_HEIGHT",
                "zoom": 18.6,
                "exponent": 52.1,
                "fracture": {
                    "style": "BIOCTAVE_FRACTAL_CUBIC",
                    "zoom": 27.0,
                    "cellularZoom": 13.08,
                    "axialFracturing": False,
                    "cellularFrequency": 0.4,
                    "exponent": 14.3,
                    "multiplier": 28.204
                }
            },
            "negative": False,
            "seed": 158
        }
    ],
    "cliffHeightMax": 64.935,
    "cliffHeightMin": 95.26,
    "cliffHeightGenerator": {
        "seed": 126,
        "bezier": False,
        "enabled": False,
        "exponent": 16.57,
        "style": {
            "style": "FRACTAL_FBM_IRIS_THICK"
        },
        "zoom": 15.0,
        "fracture": [
            {
                "bezier": False,
                "enabled": False,
                "exponent": 20.533,
                "zoom": 12.757,
                "style": {
                    "style": "PERLIN_IRIS_DOUBLE",
                    "axialFracturing": True,
                    "cellularFrequency": 29.6,
                    "cellularZoom": 10.208,
                    "exponent": 56.523,
                    "multiplier": 36.799,
                    "zoom": 19.062
                },
                "sinCentered": True,
                "negative": True,
                "seed": 44,
                "parametric": True,
                "octaves": 8,
                "offsetX": 8.2,
                "offsetY": 25.0,
                "offsetZ": 17.0,
                "opacity": 0.08
            }
        ]
    }
}

sample_json4 = {
    "interpolator": {
        "function": "HERMITE_STARCAST_12",
        "horizontalScale": 1898.256
    },
    "seed": 30,
    "composite": [
        {
            "style": {
                "style": "CELLULAR_HEIGHT",
                "zoom": 18.6,
                "exponent": 52.1,
                "fracture": {
                    "style": "BIOCTAVE_FRACTAL_CUBIC",
                    "zoom": 27.0,
                    "cellularZoom": 13.08,
                    "axialFracturing": True,
                    "cellularFrequency": 0.4,
                    "exponent": 14.3,
                    "multiplier": 28.204
                }
            },
            "negative": True,
            "seed": 158
        }
    ],
    "cellFractureHeight": 46.2,
    "cellFractureShuffle": 45.1,
    "cellFractureZoom": 17.2,
    "cellPercentSize": 0.05,
    "multiplicitive": True,
    "offsetX": 20.9,
    "offsetZ": 1.63,
    "opacity": 0.12,
    "zoom": 19.28
}


style_options = [
    "STATIC", "STATIC_BILINEAR", "STATIC_BICUBIC", "STATIC_HERMITE", "IRIS",
    "CLOVER", "CLOVER_STARCAST_3", "CLOVER_STARCAST_6", "CLOVER_STARCAST_9",
    "CLOVER_STARCAST_12", "CLOVER_BILINEAR_STARCAST_3",
    "CLOVER_BILINEAR_STARCAST_6", "CLOVER_BILINEAR_STARCAST_9",
    "CLOVER_BILINEAR_STARCAST_12", "CLOVER_HERMITE_STARCAST_3",
    "CLOVER_HERMITE_STARCAST_6", "CLOVER_HERMITE_STARCAST_9",
    "CLOVER_HERMITE_STARCAST_12", "CLOVER_BILINEAR", "CLOVER_BICUBIC",
    "CLOVER_HERMITE", "VASCULAR", "FLAT", "CELLULAR", "CELLULAR_STARCAST_3",
    "CELLULAR_STARCAST_6", "CELLULAR_STARCAST_9", "CELLULAR_STARCAST_12",
    "CELLULAR_BILINEAR_STARCAST_3", "CELLULAR_BILINEAR_STARCAST_6",
    "CELLULAR_BILINEAR_STARCAST_9", "CELLULAR_BILINEAR_STARCAST_12",
    "CELLULAR_HERMITE_STARCAST_3", "CELLULAR_HERMITE_STARCAST_6",
    "CELLULAR_HERMITE_STARCAST_9", "CELLULAR_HERMITE_STARCAST_12",
    "CELLULAR_BILINEAR", "CELLULAR_BICUBIC", "CELLULAR_HERMITE", "NOWHERE",
    "NOWHERE_CELLULAR", "NOWHERE_CLOVER", "NOWHERE_SIMPLEX", "NOWHERE_GLOB",
    "NOWHERE_VASCULAR", "NOWHERE_CUBIC", "NOWHERE_SUPERFRACTAL", "NOWHERE_FRACTAL",
    "IRIS_DOUBLE", "IRIS_THICK", "IRIS_HALF", "SIMPLEX", "FRACTAL_SMOKE",
    "VASCULAR_THIN", "SIMPLEX_CELLS", "SIMPLEX_VASCULAR", "FRACTAL_WATER",
    "PERLIN", "PERLIN_IRIS", "PERLIN_IRIS_HALF", "PERLIN_IRIS_DOUBLE",
    "PERLIN_IRIS_THICK", "FRACTAL_BILLOW_PERLIN", "BIOCTAVE_FRACTAL_BILLOW_PERLIN",
    "FRACTAL_BILLOW_SIMPLEX", "FRACTAL_FBM_SIMPLEX", "FRACTAL_BILLOW_IRIS",
    "FRACTAL_FBM_IRIS", "FRACTAL_BILLOW_IRIS_HALF", "FRACTAL_FBM_IRIS_HALF",
    "FRACTAL_BILLOW_IRIS_THICK", "FRACTAL_FBM_IRIS_THICK", "FRACTAL_RM_SIMPLEX",
    "BIOCTAVE_FRACTAL_BILLOW_SIMPLEX", "BIOCTAVE_FRACTAL_FBM_SIMPLEX",
    "BIOCTAVE_FRACTAL_RM_SIMPLEX", "TRIOCTAVE_FRACTAL_RM_SIMPLEX",
    "TRIOCTAVE_FRACTAL_BILLOW_SIMPLEX", "TRIOCTAVE_FRACTAL_FBM_SIMPLEX",
    "QUADOCTAVE_FRACTAL_RM_SIMPLEX", "QUADOCTAVE_FRACTAL_BILLOW_SIMPLEX",
    "QUADOCTAVE_FRACTAL_FBM_SIMPLEX", "QUINTOCTAVE_FRACTAL_RM_SIMPLEX",
    "QUINTOCTAVE_FRACTAL_BILLOW_SIMPLEX", "QUINTOCTAVE_FRACTAL_FBM_SIMPLEX",
    "SEXOCTAVE_FRACTAL_RM_SIMPLEX", "SEXOCTAVE_FRACTAL_BILLOW_SIMPLEX",
    "SEXOCTAVE_FRACTAL_FBM_SIMPLEX", "SEPTOCTAVE_FRACTAL_RM_SIMPLEX",
    "SEPTOCTAVE_FRACTAL_BILLOW_SIMPLEX", "SEPTOCTAVE_FRACTAL_FBM_SIMPLEX",
    "OCTOCTAVE_FRACTAL_RM_SIMPLEX", "OCTOCTAVE_FRACTAL_BILLOW_SIMPLEX",
    "OCTOCTAVE_FRACTAL_FBM_SIMPLEX", "NONOCTAVE_FRACTAL_RM_SIMPLEX",
    "NONOCTAVE_FRACTAL_BILLOW_SIMPLEX", "NONOCTAVE_FRACTAL_FBM_SIMPLEX",
    "VIGOCTAVE_FRACTAL_RM_SIMPLEX", "VIGOCTAVE_FRACTAL_BILLOW_SIMPLEX",
    "VIGOCTAVE_FRACTAL_FBM_SIMPLEX", "BIOCTAVE_SIMPLEX", "TRIOCTAVE_SIMPLEX",
    "QUADOCTAVE_SIMPLEX", "QUINTOCTAVE_SIMPLEX", "SEXOCTAVE_SIMPLEX",
    "SEPTOCTAVE_SIMPLEX", "OCTOCTAVE_SIMPLEX", "NONOCTAVE_SIMPLEX",
    "VIGOCTAVE_SIMPLEX", "GLOB", "GLOB_IRIS", "GLOB_IRIS_HALF", "GLOB_IRIS_DOUBLE",
    "GLOB_IRIS_THICK", "CUBIC", "FRACTAL_CUBIC", "FRACTAL_CUBIC_IRIS",
    "FRACTAL_CUBIC_IRIS_THICK", "FRACTAL_CUBIC_IRIS_HALF", "FRACTAL_CUBIC_IRIS_DOUBLE",
    "BIOCTAVE_FRACTAL_CUBIC", "TRIOCTAVE_FRACTAL_CUBIC", "QUADOCTAVE_FRACTAL_CUBIC",
    "CUBIC_IRIS", "CUBIC_IRIS_HALF", "CUBIC_IRIS_DOUBLE", "CUBIC_IRIS_THICK",
    "CELLULAR_IRIS", "CELLULAR_IRIS_THICK", "CELLULAR_IRIS_DOUBLE",
    "CELLULAR_IRIS_HALF", "CELLULAR_HEIGHT", "CELLULAR_HEIGHT_IRIS",
    "CELLULAR_HEIGHT_IRIS_DOUBLE", "CELLULAR_HEIGHT_IRIS_THICK", "CELLULAR_HEIGHT_IRIS_HALF",
    "VASCULAR_IRIS", "VASCULAR_IRIS_DOUBLE", "VASCULAR_IRIS_THICK", "VASCULAR_IRIS_HALF"
]
function_options = [
    "BILINEAR", "STARCAST_3", "STARCAST_6", "STARCAST_9", "STARCAST_12",
    "BILINEAR_STARCAST_3", "BILINEAR_STARCAST_6", "BILINEAR_STARCAST_9",
    "BILINEAR_STARCAST_12", "HERMITE_STARCAST_3", "HERMITE_STARCAST_6",
    "HERMITE_STARCAST_9", "HERMITE_STARCAST_12", "BILINEAR_BEZIER",
    "BILINEAR_PARAMETRIC_2", "BILINEAR_PARAMETRIC_4", "BILINEAR_PARAMETRIC_1_5",
    "BICUBIC", "HERMITE", "CATMULL_ROM_SPLINE", "HERMITE_TENSE",
    "HERMITE_LOOSE", "HERMITE_LOOSE_HALF_POSITIVE_BIAS",
    "HERMITE_LOOSE_HALF_NEGATIVE_BIAS", "HERMITE_LOOSE_FULL_POSITIVE_BIAS",
    "HERMITE_LOOSE_FULL_NEGATIVE_BIAS",
]

selected_template = select_template()
randomized_file_path = randomize_json_and_save_with_random_name(r"Your\Path", selected_template) # Your path goes here, if you are using / slashes, remove the prefix "r" before the double quotes.
print(f"Randomized JSON saved to: {randomized_file_path}")
