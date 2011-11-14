$(function () {
/*
	var data = [
		{ label: "Accepted" , data: 200 },
		{ label: "Declined" , data:  50 },
		{ label: "Completed", data: 100 }
	]
*/	
	// Query for the quest statistics
	var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];
	
	$.plot($('#completion_times'), [{
		data: d2,
		bars: { show: true }
	}]);
	
	// Create the status information
	var status_options =
	{
		series:
		{
			pie: { show: true }
		}
	}
	
	var status_data = [];
	
	$.plot($('#completed_pie'), status_data, status_options);
	
	function onStatisticsDataReceived(statistics)
	{
		$('#average_completion').text(statistics.average_completion);
		$('#shortest_completion').text(statistics.shortest_completion);
		$('#longest_completion').text(statistics.longest_completion);
		
		$.plot($('#completed_pie'), statistics.status, status_options);
	}
	
	var test1 =
	{
		'average_completion' : '1:34:00',
		'shortest_completion': '0:05:00',
		'longest_completion' : '5:22:00',
		'status':
		[
			{ label: "Accepted" , data: 100 },
			{ label: "Declined" , data: 500 },
			{ label: "Completed", data: 350 }
		]
	};
	
	var test2 =
	{
		'average_completion' : '2:44:00',
		'shortest_completion': '0:15:00',
		'longest_completion' : '9:22:00',
		'status':
		[
			{ label: "Accepted" , data: 200 },
			{ label: "Declined" , data:  50 },
			{ label: "Completed", data: 100 }
		]
	};
	
	onStatisticsDataReceived(test1);
	
	// Trigger request when the Quest option changes
	$('#quests').change(function() {
		$.ajax({
			url: '/quest_statistics/',
			method: 'GET',
			dataType: 'json',
			success: onStatisticsDataReceived
		});
	});
});