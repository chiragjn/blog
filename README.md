# The Digital Paper Blog Source

http://chiragjn.github.io/blog/

Blog based on Pelican

content/ and github_content/ folder intentionally removed.

Run `make regenerate` to generate output

Run `make devserver` to start server locally

Run `make publish` to generate output for github

To push 

```
cd github_output/
git add .
git commit -m "Blog Update"
git push origin gh-pages
```