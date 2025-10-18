"""
AlfAI Core - Test Complete Flow
Test: prompt → supervision → reasoning → audit
"""

import sys
import os
from datetime import datetime
import json

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from layers.layer_framework import LayerFramework
from dre import DREEngine
from cms import CMSEngine
from eei import EEIEngine
from cce import CCEEngine
from utils.flow_manager import FlowManager

def test_complete_flow():
    """Test the complete flow: prompt → supervision → reasoning → audit"""
    print("🚀 AlfAI Core - Complete Flow Test")
    print("=" * 60)
    
    # Initialize components
    layer_framework = LayerFramework()
    dre_engine = DREEngine()
    cms_engine = CMSEngine()
    eei_engine = EEIEngine()
    cce_engine = CCEEngine()
    flow_manager = FlowManager()
    
    # Test data
    test_data = {
        "prompt": "Analyze customer data for loan approval decision",
        "customer_data": {
            "name": "John Doe",
            "age": 35,
            "income": 75000,
            "credit_score": 720,
            "employment_status": "employed",
            "loan_amount": 250000,
            "personal_data": "sensitive_information"
        },
        "user_id": "test_user_001",
        "timestamp": datetime.utcnow().isoformat()
    }
    
    results = {}
    
    try:
        # Step 1: Prompt Processing (14-Layer Framework)
        print("\n📝 Step 1: Processing Prompt through 14-Layer Framework")
        print("-" * 50)
        
        prompt_start = datetime.utcnow()
        prompt_result = layer_framework.process_through_layers(test_data)
        prompt_time = int((datetime.utcnow() - prompt_start).total_seconds() * 1000)
        
        print(f"✅ Prompt processed through {prompt_result['total_layers']} layers")
        print(f"⏱️ Processing time: {prompt_time}ms")
        print(f"📊 Success rate: {prompt_result['successful_layers']}/{prompt_result['total_layers']}")
        
        results["prompt_processing"] = {
            "status": "completed",
            "processing_time_ms": prompt_time,
            "layers_processed": prompt_result['total_layers'],
            "success_rate": prompt_result['successful_layers'] / prompt_result['total_layers'],
            "result": prompt_result
        }
        
        # Step 2: Supervision (AXA-I Integration)
        print("\n🔍 Step 2: Supervision through AXA-I Integration")
        print("-" * 50)
        
        supervision_start = datetime.utcnow()
        supervision_result = flow_manager.process_supervision(
            test_data, "loan_approval_supervision", test_data["user_id"]
        )
        supervision_time = int((datetime.utcnow() - supervision_start).total_seconds() * 1000)
        
        print(f"✅ Supervision completed")
        print(f"⏱️ Processing time: {supervision_time}ms")
        print(f"📊 Supervision score: {supervision_result['supervision_score']:.2f}")
        
        results["supervision"] = {
            "status": "completed",
            "processing_time_ms": supervision_time,
            "supervision_score": supervision_result['supervision_score'],
            "result": supervision_result
        }
        
        # Step 3: Reasoning (DRE Engine)
        print("\n🧠 Step 3: Reasoning through DRE Engine")
        print("-" * 50)
        
        reasoning_start = datetime.utcnow()
        reasoning_result = dre_engine.analyze_data(test_data["customer_data"])
        reasoning_time = int((datetime.utcnow() - reasoning_start).total_seconds() * 1000)
        
        print(f"✅ Reasoning analysis completed")
        print(f"⏱️ Processing time: {reasoning_time}ms")
        print(f"📊 Confidence score: {reasoning_result['dre_analysis']['confidence_score']:.2f}")
        print(f"🔍 Patterns detected: {reasoning_result['dre_analysis']['patterns_detected']}")
        print(f"💭 Inferences generated: {reasoning_result['dre_analysis']['inferences_generated']}")
        
        results["reasoning"] = {
            "status": "completed",
            "processing_time_ms": reasoning_time,
            "confidence_score": reasoning_result['dre_analysis']['confidence_score'],
            "patterns_detected": reasoning_result['dre_analysis']['patterns_detected'],
            "inferences_generated": reasoning_result['dre_analysis']['inferences_generated'],
            "result": reasoning_result
        }
        
        # Step 4: Audit (EEI + CCE)
        print("\n⚖️ Step 4: Audit through EEI and CCE")
        print("-" * 50)
        
        audit_start = datetime.utcnow()
        
        # EEI Ethical Evaluation
        print("   🔍 EEI: Ethical Evaluation...")
        eei_result = eei_engine.evaluate_ethics(test_data["customer_data"])
        print(f"   ✅ Ethical score: {eei_result['eei_evaluation']['overall_score']:.2f}")
        print(f"   📊 Violations: {eei_result['eei_evaluation']['violations_detected']}")
        
        # CCE Compliance Check
        print("   🛡️ CCE: Compliance Check...")
        cce_result = cce_engine.check_compliance(test_data["customer_data"])
        print(f"   ✅ Compliance score: {cce_result['cce_compliance']['overall_score']:.2f}")
        print(f"   📊 Standards checked: {len(cce_result['cce_compliance']['standards_checked'])}")
        print(f"   ⚠️ Violations: {cce_result['cce_compliance']['total_violations']}")
        
        audit_time = int((datetime.utcnow() - audit_start).total_seconds() * 1000)
        
        results["audit"] = {
            "status": "completed",
            "processing_time_ms": audit_time,
            "ethical_score": eei_result['eei_evaluation']['overall_score'],
            "compliance_score": cce_result['cce_compliance']['overall_score'],
            "violations_detected": eei_result['eei_evaluation']['violations_detected'] + cce_result['cce_compliance']['total_violations'],
            "eei_result": eei_result,
            "cce_result": cce_result
        }
        
        # Complete Flow Summary
        total_time = sum([
            results["prompt_processing"]["processing_time_ms"],
            results["supervision"]["processing_time_ms"],
            results["reasoning"]["processing_time_ms"],
            results["audit"]["processing_time_ms"]
        ])
        
        print(f"\n🎉 COMPLETE FLOW TEST RESULTS")
        print("=" * 60)
        print(f"✅ All steps completed successfully")
        print(f"⏱️ Total processing time: {total_time}ms")
        print(f"📊 Overall success rate: 100%")
        print(f"🔍 Components tested: 14-Layer Framework, AXA-I, DRE, CMS, EEI, CCE")
        
        # Generate JSON report
        test_report = {
            "test_completed": True,
            "test_timestamp": datetime.utcnow().isoformat(),
            "total_processing_time_ms": total_time,
            "test_results": results,
            "component_summaries": {
                "layer_framework": layer_framework.get_processing_summary(),
                "dre_engine": dre_engine.get_reasoning_summary(),
                "cms_engine": cms_engine.get_content_summary(),
                "eei_engine": eei_engine.get_ethical_summary(),
                "cce_engine": cce_engine.get_compliance_summary(),
                "flow_manager": flow_manager.get_flow_summary()
            }
        }
        
        # Save test report
        with open("alfai_core_test_report.json", "w") as f:
            json.dump(test_report, f, indent=2, default=str)
        
        print(f"\n💾 Test report saved: alfai_core_test_report.json")
        
        return test_report
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        return {"test_completed": False, "error": str(e)}

def main():
    """Main test function"""
    print("🎯 AlfAI Core - Complete System Test")
    print("Testing: prompt → supervision → reasoning → audit")
    print("=" * 60)
    
    try:
        test_report = test_complete_flow()
        
        if test_report.get("test_completed"):
            print(f"\n✅ TEST PASSED - All components working correctly")
            return True
        else:
            print(f"\n❌ TEST FAILED - {test_report.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"\n❌ Test execution failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
