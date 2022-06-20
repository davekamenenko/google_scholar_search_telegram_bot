import unittest
from serpapi import GoogleSearch
import  sqlite3

class MyTestCase(unittest.TestCase):
    def test_title_check(self):
        params["q"] = 'test'
        search = GoogleSearch(params)
        results = search.get_dict()
        self.assertEqual(str(results['organic_results'][i]['title'])
        with self.assertRaises(TypeError):
            type(str(results['organic_results'][i]['title'])

    def test_bdcon(self):
        self.assertTrue(conn = sqlite3.connect('bd.db'))
        self.assertTrue(cursor = conn.cursor())
        self.assertTrue(query = cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (message.from_user.id,)))

    def tanimoto(s1, s2):
        a, b, c = len(s1), len(s2), 0.0

        for sym in s1:
            if sym in s2:
                c += 1

        return c / (a + b - c)
    def test_tanimoto(self): \
            self.assertEqual(1,2)
            self.assertEqual(1.2,2)
            self.assertEqual(1.6,2)



if __name__ == '__main__':
    unittest.main()
