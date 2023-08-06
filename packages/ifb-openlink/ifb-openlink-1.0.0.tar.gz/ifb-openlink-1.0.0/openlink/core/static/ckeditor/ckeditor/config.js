/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

 CKEDITOR.editorConfig = function( config ) {
	config.toolbar = 'ZenodoToolbar';
        config.toolbar_ZenodoToolbar =[
		{ name: 'clipboard', items: [ 'PasteText', 'PasteFromWord',] },
		
		{ name: 'basicstyles', items: [ 'Bold', 'Italic', 'Strike', 'Subscript', 'Superscript', '-',] },
		{ name: 'links', items: [ 'Link', 'Unlink', ] },
		
		{ name: 'paragraph', items: [ 'NumberedList', 'BulletedList', 'Outdent', 'Indent', 'Blockquote','CodeSnippet'] },
		{ name: 'undo', groups: [ 'clipboard', 'undo' ], items: ['Undo','Redo','RemoveFormat']},
		{ name: 'insert', items: ['SpecialChar','Mathjax'] },
		
		{ name: 'document', items: [ 'Source']},
		{ name: 'tools', items: [ 'Maximize', ]}
	];
};
