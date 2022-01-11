{
    "name": "simplecollapsible",
    "displayName": "Simple Collapsible",
    "version": 1,
    "icon": "12grid/simplecollapsible/simplecollapsible.png",
    "definition": "simplecollapsible/simplecollapsible.json",
    "categoryName": "Templates",
	"excludes": ["container","column","flexitem"],
	"designStyleClass" : "simplecollapsibleDesign",
    "topContainer": true,
    "directives": ["gridCollapse"],
    "tagType":"div",
    "model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" }}
	}
}