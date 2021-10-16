# jounileino.com

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

### Development

| Command         | Action                                      |
|:----------------|:--------------------------------------------|
| `npm install`   | Installs dependencies                       |
| `npm run dev`   | Starts local dev server at `localhost:3000` |

### Deployment

| Command                               | Action                                      |
|:--------------------------------------|:--------------------------------------------|
| `npm run build`                       | Build your production site to `./dist/`     |
| `cd dist`                             | Navigate to dist directory                  |
| `aws s3 sync . s3://jounileino.com`   | Deploys static website to AWS S3            |

