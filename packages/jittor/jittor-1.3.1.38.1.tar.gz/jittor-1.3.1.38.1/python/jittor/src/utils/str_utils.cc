// ***************************************************************
// Copyright (c) 2021 Jittor. All Rights Reserved. 
// Maintainers: Dun Liang <randonlang@gmail.com>. 
// This file is subject to the terms and conditions defined in
// file 'LICENSE.txt', which is part of this source code package.
// ***************************************************************
#include "utils/str_utils.h"

namespace jittor {


bool startswith(const string& a, const string& b, uint start, bool equal, uint end) {
    if (!end) end = a.size();
    if (b.size()+start > end) return false;
    if (equal && b.size()+start != end) return false;
    for (uint i=0; i<b.size(); i++)
        if (a[i+start] != b[i]) return false;
    return true;
}

bool endswith(const string& a, const string& b) {
    if (a.size() < b.size()) return false;
    return startswith(a, b, a.size()-b.size());
}

vector<string> split(const string& s, const string& sep, int max_split) {
    vector<string> ret;
    int pos = 0, pos_next;
    while (1) {
        pos_next = s.find(sep, pos);
        if (pos_next == (int)string::npos || (int)ret.size() == max_split-1) {
            ret.push_back(s.substr(pos));
            return ret;
        }
        ret.push_back(s.substr(pos, pos_next-pos));
        pos = pos_next + sep.size();
    }
    ASSERT(max_split==0);
    return ret;
}

string strip(const string& s) {
    int i=0;
    while (i<s.size() && (s[i]==' ' || s[i]=='\t' || s[i]=='\n' || s[i]=='\r')) i++;
    int j = s.size();
    while (j>i && (s[j-1]==' ' || s[j-1]=='\t' || s[j-1]=='\n' || s[j-1]=='\r')) j--;
    return s.substr(i,j-i);
}

string format(const string& s, const vector<string>& v) {
    string ss;
    for (int i=0; i<s.size(); i++) {
        if (s[i] == '$') {
            int j = s[i+1] - '0';
            ss += v.at(j);
            i ++;
            continue;
        } else
            ss += s[i];
    }
    return ss;
}

string join(const vector<string>& vs, const string& x) {
    string s;
    for (int i=0; i<vs.size(); i++) {
        s += vs[i];
        if (i!=vs.size()-1)
            s += x;
    }
    return s;
}

string replace(const string& a, const string& b, const string& c) {
    auto vs = split(a, b);
    return join(vs, c);
}

} // jittor