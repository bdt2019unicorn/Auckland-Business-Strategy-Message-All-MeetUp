using System;
using Newtonsoft.Json;
using System.Data;
using System.IO;
using ClosedXML.Excel;

namespace ConvertJsonToExcel
{
    class Program
    {
        static string group_name = "Young-NZ-Business-Professionals-Network"; 
        static DataTable DataFromJson(string file_name)
        {
            string json_string = File.ReadAllText(file_name);
            string[] all_links = JsonConvert.DeserializeObject<string[]>(json_string);

            DataTable data = new DataTable();
            data.Columns.Add("Links"); 
            foreach (string link in all_links)
            {
                DataRow row = data.NewRow();
                row["Links"] = link;
                data.Rows.Add(row); 
            }
            return data; 
        }

        static void DataToExcel(DataTable data)
        {
            XLWorkbook wb = new XLWorkbook();
            wb.Worksheets.Add(data, "Links");
            wb.SaveAs(group_name+".xlsx"); 
        }

        static void Main(string[] args)
        {
            DataTable json_data = DataFromJson(group_name+".json");
            DataToExcel(json_data); 
        }
    }
}
