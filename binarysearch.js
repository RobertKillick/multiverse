function binary_search(x, sorted_collection, low = 0, high = null) {
    if (high === null) {
      high = sorted_collection.length;
    } else if (high < 0) {
      throw new RangeError('High index out of range');
    }
  
    if (low > high) return null;
  
    const mid = Math.floor((high + low) / 2);
    const value = sorted_collection[mid];
  
    if (value == x) {
      return value;
    } else if (value > x) {
      return binary_search(x, sorted_collection, mid + 1, high);
    } else {
      return binary_search(x, sorted_collection, low, mid - 1);
    }
  }
  
  // Don't change anything below this line ;)
  
  const tests = [
    {
      find: 1,
      collection: [],
      expected: null
    },
    {
      find: 1,
      collection: [1],
      expected: 0
    },
    {
      find: 2,
      collection: [1],
      expected: null
    },
    {
      find: 1,
      collection: [1, 2],
      expected: 0
    },
    {
      find: 2,
      collection: [1, 2],
      expected: 1
    },
    {
      find: 3,
      collection: [1, 2, 3],
      expected: 2
    },
    {
      find: 1,
      collection: [1, 2, 3, 4],
      expected: 0
    },
    {
      find: 2,
      collection: [1, 2, 3, 4],
      expected: 1
    },
    {
      find: 3,
      collection: [1, 2, 3, 4],
      expected: 2
    },
    {
      find: 4,
      collection: [1, 2, 3, 4],
      expected: 3
    },
    {
      find: 1,
      collection: [1, 2, 3, 4, 5],
      expected: 0
    },
    {
      find: 2,
      collection: [1, 2, 3, 4, 5],
      expected: 1
    },
    {
      find: 3,
      collection: [1, 2, 3, 4, 5],
      expected: 2
    },
    {
      find: 4,
      collection: [1, 2, 3, 4, 5],
      expected: 3
    },
    {
      find: 5,
      collection: [1, 2, 3, 4, 5],
      expected: 4
    },
    {
      find: 99,
      collection: [1, 2, 3, 4, 5],
      expected: null
    }
  ];
  
  const results = tests.map(function(test) {
    try {
      var result = binary_search(test['find'], test['collection']);
      test.result = result;
      test.success = result == test['expected'];
    } catch (ex) {
      test.result = ex.message;
      test.success = false;
    }
  
    return test
  });
  
  console.table(results);