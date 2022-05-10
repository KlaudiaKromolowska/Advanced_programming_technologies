const path = require( 'path' );
const webpack = require( 'webpack' );

module.exports = ( env, options ) => {
    return {
        entry: './index.js',

        output: {
            path: path.resolve( __dirname, 'build' ),
            filename: 'build.js',
        },
    }
};