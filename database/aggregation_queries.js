// Top Edited Pages
db.wiki_events.aggregate([
  {
    $group: {
      _id: "$title",
      total_edits: { $sum: 1 }
    }
  },
  {
    $sort: { total_edits: -1 }
  },
  {
    $limit: 10
  }
])

// Most Active Users
db.wiki_events.aggregate([
  {
    $group: {
      _id: "$user",
      edits: { $sum: 1 }
    }
  },
  {
    $sort: { edits: -1 }
  }
])

// Bot vs Human Activity
db.wiki_events.aggregate([
  {
    $group: {
      _id: "$bot",
      total: { $sum: 1 }
    }
  }
])