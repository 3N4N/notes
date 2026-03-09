# directories
SRC_DIR = .
OUT_DIR = site
# CSS_DIR = 
STYLES := tufte.css \
					pandoc.css \
					tufte-extra.css


# find markdown files
MD_FILES := $(shell find $(SRC_DIR) -name '*.md')

# convert paths to html output paths
HTML_FILES := $(patsubst $(SRC_DIR)/%.md,$(OUT_DIR)/%.html,$(MD_FILES))

# default target
all: $(HTML_FILES) index
	cp -r css site

# rule to build each html file
$(OUT_DIR)/%.html: $(SRC_DIR)/%.md
	mkdir -p $(dir $@)
	pandoc $< -o $@ --toc --standalone -f markdown+smart --to=html5+smart \
		--template templates/tufte \
		$(foreach style,$(STYLES),--css ../../css/$(style))
		# -c ../css/pandoc.css -c ../css/tufte.css -c ../css/tufte-extra.css

# generate index
index:
	python make_index.py

# rebuild everything
rebuild: clean all

# clean output
clean:
	rm -rf $(OUT_DIR)
	rm -f index.html

.PHONY: all clean rebuild index
