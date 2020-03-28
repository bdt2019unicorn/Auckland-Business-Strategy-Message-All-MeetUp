using System;
using Newtonsoft.Json;
using System.Data;
using System.IO;
using ClosedXML.Excel;

namespace ConvertJsonToExcel
{
    class Program
    {
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
            wb.Worksheets.Add(data, "Auckland Bussiness Strategies");
            wb.SaveAs("Auckland Bussiness Strategies.xlsx"); 
        }

        static void Main(string[] args)
        {
            string file_name = "links.json";
            DataTable json_data = DataFromJson(file_name);
            DataToExcel(json_data); 
        }
    }
}
