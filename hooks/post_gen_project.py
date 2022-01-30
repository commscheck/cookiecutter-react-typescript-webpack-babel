import subprocess

subprocess.run(["yarn", "add", "react", "react-dom"], check=True)
subprocess.run(
    [
        "yarn",
        "add",
        "--dev",
        "@babel/core",
        "@babel/node",
        "@babel/preset-env",
        "@babel/preset-react",
        "@babel/preset-typescript",
        "@types/react-dom",
        "@types/react",
        "@typescript-eslint/eslint-plugin",
        "@typescript-eslint/parser",
        "babel-loader",
        "css-loader",
        "eslint-config-prettier",
        "eslint-plugin-react",
        "eslint",
        "html-webpack-plugin",
        "mini-css-extract-plugin",
        "prettier",
        "style-loader",
        "typescript",
        "webpack-cli",
        "webpack-dev-server",
        "webpack",
    ],
    check=True,
)
