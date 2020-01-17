

(function ($) {
    //    "use strict";


    /*  Data Table
	-------------*/
	// table.destroy();


	// // Setup a fixed size for the first column of table
	// $('#bootstrap-data-table-loan-detail').dataTable( {
	// 	// "destroy": true,
	// 	"columnDefs": [
	// 	  { "width": "20px", "targets": 0 }
	// 	],
	// 	"lengthMenu": [[10, 20, 50, -1], [10, 20, 50, "All"]],
	// 	"searching": false,
	// 	"info": false,
	// 	// "paging": false
	//   } );

	// Setup a fixed size for the first column of table
	$('#bootstrap-data-table-export').DataTable( {
		"columnDefs": [
		  { "width": "20px", "targets": 0 }
		],
		"lengthMenu": [[10, 20, 50, -1], [10, 20, 50, "All"]],
		"bLengthChange" : false,  // disable the page option
		"initComplete" : function() {
			var input = $('.dataTables_filter input').unbind(),
				self = this.api(),
				$searchButton = $('<button class="btn btn-outline-secondary mr-1 ml-1">')
						   .text('Search')
						   .click(function() {
							  self.search(input.val()).draw();
						   })
			$('.dataTables_filter')
				.append($searchButton);
			
		}       
	  } );

    // $('#bootstrap-data-table').DataTable({
    //     lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
	// });
	
	// if ( $.fn.dataTable.isDataTable( '#bootstrap-data-table-export' ) ) {
	// 	table = $('#bootstrap-data-table-export').DataTable();
	// }
	// else {
	// 	table = $('#bootstrap-data-table-export').DataTable( {
	// 		lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    //     	buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
	// 	} );
	// }

    // // $('#bootstrap-data-table-export').DataTable({
    // //     lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    // //     buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
    // // });

	// $('#row-select').DataTable( {
    //     initComplete: function () {
	// 			this.api().columns().every( function () {
	// 				var column = this;
	// 				var select = $('<select class="form-control"><option value=""></option></select>')
	// 					.appendTo( $(column.footer()).empty() )
	// 					.on( 'change', function () {
	// 						var val = $.fn.dataTable.util.escapeRegex(
	// 							$(this).val()
	// 						);

	// 						column
	// 							.search( val ? '^'+val+'$' : '', true, false )
	// 							.draw();
	// 					} );

	// 				column.data().unique().sort().each( function ( d, j ) {
	// 					select.append( '<option value="'+d+'">'+d+'</option>' )
	// 				} );
	// 			} );
	// 		}
	// 	} );

	// $('#bootstrap-data-table-export').DataTable({
	// 	initComplete : function() {
	// 		var input = $('.dataTables_filter input').unbind(),
	// 			self = this.api(),
	// 			$searchButton = $('<button>')
	// 					   .text('search')
	// 					   .click(function() {
	// 						  self.search(input.val()).draw();
	// 					   }),
	// 			$clearButton = $('<button>')
	// 					   .text('clear')
	// 					   .click(function() {
	// 						  input.val('');
	// 						  $searchButton.click(); 
	// 					   }) 
	// 		$('.dataTables_filter').append($searchButton, $clearButton);
	// 	}            
	// });


})(jQuery);
