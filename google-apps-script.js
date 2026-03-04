/**
 * Google Apps Script - Lead Capture Backend
 * 
 * SETUP INSTRUCTIONS:
 * 1. Go to https://sheets.google.com and create a new spreadsheet
 * 2. Name it "AI Money Earning - Leads"
 * 3. In Row 1, add these headers: Timestamp | Name | Email | Phone | Language | UTM Source | UTM Medium | UTM Campaign | UTM Content | UTM Term
 * 4. Go to Extensions → Apps Script
 * 5. Delete the default code and paste this entire file
 * 6. Click Deploy → New Deployment
 * 7. Select "Web app"
 * 8. Set "Execute as" = "Me" and "Who has access" = "Anyone"
 * 9. Click Deploy and copy the Web App URL
 * 10. Paste that URL in ta/index.html and en/index.html (replace GOOGLE_SCRIPT_URL)
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    
    sheet.appendRow([
      new Date().toISOString(),
      data.name || '',
      data.email || '',
      data.phone || '',
      data.lang || '',
      data.utm_source || '',
      data.utm_medium || '',
      data.utm_campaign || '',
      data.utm_content || '',
      data.utm_term || ''
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', message: 'Lead capture endpoint is active' }))
    .setMimeType(ContentService.MimeType.JSON);
}
