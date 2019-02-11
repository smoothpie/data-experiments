const path = require('path')
const HtmlWebPackPlugin = require('html-webpack-plugin')

let sourcePath = path.join(__dirname, "./client");

module.exports = {
  entry: {
    main: './client/index.js',
  },
  output: {
    filename: '[name].[hash].js',
    path: path.resolve('./dist'),
    publicPath: '/'
  },
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx", ".json"],
    mainFields: ["main", "index"],
    alias: {
      containers: path.resolve(sourcePath, "containers/"),
      components: path.resolve(sourcePath, "components/"),
    }
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: ['node_modules'],
        loader: require.resolve('babel-loader'),
        options: {
          cacheDirectory: true,
          plugins: ['react-hot-loader/babel'],
        },
      },
      {
        test: /\.(jpe?g|png|gif|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "url-loader",
        options: {
          limit: 25000,
        }
      },
      {
        test: [/\.css$/, /\.scss$/],
        exclude: ['node_modules'],
        use: [
          {
            loader: "style-loader"
          },
          {
            loader: "css-loader"
          },
        ]
      }
    ]
  },
  plugins: [
    new HtmlWebPackPlugin({
      template: 'index.html'
    }),
  ],
  devServer: {
    host: 'localhost',
    port: 3000,
    open: true,
    historyApiFallback: true
  }
}