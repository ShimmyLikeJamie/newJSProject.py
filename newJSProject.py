import sys
import os
import subprocess

html_structure = """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="styles/style.css" />
  </head>
  <body>
    <div id="container"></div>
  </body>
  <footer>
    <script src="bundle.js"></script>
  </footer>
</html>
"""

webpack_config = """
// Generated using webpack-cli http://github.com/webpack-cli
const path = require('path');

module.exports = {
    mode: 'development',
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    plugins: [
        // Add your plugins here
        // Learn more obout plugins from https://webpack.js.org/configuration/plugins/
    ],
    module: {
        rules: [  
            // Add your rules for custom modules here
            // Learn more about loaders from https://webpack.js.org/loaders/
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ],
    },
};
"""

babel_config = """
{
  "presets": ["@babel/preset-env"]
}
"""

index_js_config = """
import 'babel-polyfill';
console.log('test')
"""

cwd = os.getcwd()

# Grab name for project if it's not included in the CLI args
confirm = False
while confirm == False:
  if (len(sys.argv) == 2):
    projectName = sys.argv[1]
  else: 
    projectName = input("Please enter a project name: ")
  userConfirm = input("Use " + projectName + " as the project name? (y/n): ")
  if userConfirm.lower() == 'y':
    confirm = True
print("Using " + projectName + " as a project name")

# Make project directory and navigate into it
subprocess.call(["mkdir", os.path.join(cwd, projectName)])
os.chdir(os.path.join(cwd, projectName))

# Initialize npm, and install webpack and babel
print("Initializing npm")
subprocess.call(["npm", "init", "-y"])
print("Installing webpack")
subprocess.call(["npm", "install", "--save-dev", "webpack", "webpack-cli"])
print("Installing babel")
subprocess.call(["npm", "install", "--save-dev", "@babel/core", "@babel/cli", "@babel/preset-env"])
subprocess.call(["npm", "install", "install", "babel-polyfill"])
subprocess.call(["npm", "install", "babel-loader"])

# Make rest of files/folders
subprocess.call(["mkdir", "dist"])
subprocess.call(["mkdir", "src"])
subprocess.call(["touch", "dist/index.html"])
subprocess.call(["mkdir", "dist/styles"])
subprocess.call(["mkdir", "dist/styles/media"])
subprocess.call(["touch", "dist/styles/style.css"])
subprocess.call(["touch", "src/index.js"])
subprocess.call(["touch", "webpack.config.js"])
subprocess.call(["touch", "babel.config.json"])

# Open and write to webpack.config.js
with open("webpack.config.js", "w") as file:
    file.write(webpack_config)
    
# Open and write to babel.config.json
with open("babel.config.json", "w") as file:
    file.write(babel_config)
    
# Open and write to index.html
with open("dist/index.html", "w") as file:
    file.write(html_structure)
    
# Open and write to index.js
with open("src/index.js", "w") as file:
    file.write(index_js_config)