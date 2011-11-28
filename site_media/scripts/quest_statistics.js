$(function () {

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
	
	function onStatisticsDataReceived(stats)
	{
		$('#accepted_count').text(stats.accepted)
		$('#rejected_count').text(stats.rejected)
		$('#completed_count').text(stats.completed)
		$('#not_encountered_count').text(stats.not_encountered)
		$('#average_completion').text(stats.average_completion);
		$('#shortest_completion').text(stats.shortest_completion);
		$('#longest_completion').text(stats.longest_completion);
		
		$.plot($('#completed_pie'), stats.status, status_options);
	}
	
	function getStatisticsData()
	{
		$.ajax({
			url: '/quest_statistics/' + $('#quests').val(),
			method: 'GET',
			dataType: 'json',
			success: onStatisticsDataReceived
		});
	}
	
	// Trigger request when the Quest option changes
	$('#quests').change(function() {
		getStatisticsData()
	});
	
	getStatisticsData()
	
});