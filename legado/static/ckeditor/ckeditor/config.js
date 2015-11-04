/**
 * Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
    // Define changes to default configuration here.
    // For the complete reference:
    // http://docs.ckeditor.com/#!/api/CKEDITOR.config

   // // Comment the following line in DEBUG mode:
   // config.removePlugins = 'devtools';
   //
   // // See the most common block elements.
   // config.format_tags = 'p;h1;h2;h3;pre';
   //
   // // Make dialogs simpler.
   // //config.removeDialogTabs = 'image:advanced;image:Link;link:advanced;link:upload';
   //// config.linkShowTargetTab = false;
   //
   // // In CKEditor 4.1 or higher you need to disable ACF (Advanced Content Filter)
   // // to make Youtube plugin work:
   // config.allowedContent = true;
};
//
//CKEDITOR.on( 'dialogDefinition', function( ev )
//   {
//      // Take the dialog name and its definition from the event data.
//      var dialogName = ev.data.name;
//      var dialogDefinition = ev.data.definition;
//
//      // Check if the definition is from the dialog we're
//      // interested in (the 'image' dialog). This dialog name found using DevTools plugin
//      if ( dialogName == 'image' )
//      {
//         // Remove the 'Link' and 'Advanced' tabs from the 'Image' dialog.
//         dialogDefinition.removeContents( 'link' );
//         dialogDefinition.removeContents( 'advanced' );
//
//         // Get a reference to the 'Image Info' tab.
//         var infoTab = dialogDefinition.getContents( 'info' );
//
//         // Remove unnecessary widgets/elements from the 'Image Info' tab.
//         infoTab.remove( 'txtHSpace');
//         infoTab.remove( 'txtVSpace');
//      }
//   });