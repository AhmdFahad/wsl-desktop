using System.Net;
using System.Net.Http;
using System.IO;
using Newtonsoft.Json;
using System.Net.Http.Headers;

namespace wsl_gui
{
    public partial class Form1 : Form
    {
        string url;
        List<Distribution> Distributions;
        public Form1()
        {
            InitializeComponent();
            url = "http://127.0.0.1:8000/wsl/api/v1/distribution";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            load();
        }

        public void load() {
            listBox1.Items.Clear();
            HttpWebRequest request = HttpWebRequest.CreateHttp(url);
            var response = request.GetResponse();
            StreamReader reader=new StreamReader(response.GetResponseStream());
            string json=reader.ReadToEnd();
            Distributions = JsonConvert.DeserializeObject<List<Distribution>>(json);

            foreach (var Distribution in Distributions)
            { 
                listBox1.Items.Add(Distribution.name);
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label2.Text=Distributions[listBox1.SelectedIndex].version;
            label3.Text=Distributions[listBox1.SelectedIndex].status;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i=listBox1.SelectedIndex;
            HttpClient httpClient= new HttpClient();
            var content = new StringContent("");
            httpClient.PostAsync("http://127.0.0.1:8000/wsl/api/v1/distribution/"+i,content);
            load();


        }
    }
    class Distribution
    {
        public string name { get; set; }
        public string version { get; set; }
        public string status { get; set; }
    }
}